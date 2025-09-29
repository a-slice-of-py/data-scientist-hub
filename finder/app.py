# /// script
# [tool.marimo.display]
# theme = "dark"
# cell_output = "below"
# ///

import marimo

__generated_with = "0.16.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from umap import UMAP
    from embetter.text import learn_lite_text_embeddings
    from sklearn.metrics.pairwise import cosine_similarity
    from model2vec import StaticModel
    import re
    import datamapplot
    return (
        StaticModel,
        UMAP,
        cosine_similarity,
        datamapplot,
        learn_lite_text_embeddings,
        mo,
        pd,
        re,
    )


@app.cell
def _(pd):
    df = pd.read_json("index.json")
    texts = (
        (
            df["category"]
            + " "
            + df["topic"].fillna("")
            + ", "
            + df["section"].fillna("")
            + " ➜ "
            + df["link_name"]
        )
        .str.replace(", : ", ": ")
        .tolist()
    )
    return df, texts


@app.cell
def _(mo):
    selected_model = mo.ui.radio(
        options=["TF-IDF", "Potion"],
        value="Potion",
        inline=True,
    )
    return (selected_model,)


@app.cell
def _(StaticModel, learn_lite_text_embeddings, selected_model, texts):
    if selected_model.value == "TF-IDF":
        embedder = learn_lite_text_embeddings(texts, dim=300)
        embeddings = embedder.transform(texts)
        handler = "transform"
    else:
        embedder = StaticModel.from_pretrained("./potion")
        embeddings = embedder.encode(texts)
        handler = "encode"
    return embedder, embeddings, handler


@app.cell
def _():
    # model = StaticModel.from_pretrained("minishlab/potion-base-8M")
    # model.save_pretrained("./potion")
    return


@app.cell
def _(UMAP, embeddings):
    X = UMAP(metric="cosine").fit_transform(embeddings)
    return (X,)


@app.cell
def _(mo):
    query = mo.ui.text(
        label="### **Search**",
        placeholder="Use - to exclude terms, # for filter categories",
        full_width=True,
    )
    return (query,)


@app.cell
def _(query, re):
    terms_to_ignore = [r.replace("-", "") for r in re.findall(r"-\w+", query.value)]
    return (terms_to_ignore,)


@app.cell
def _(embedder, handler, terms_to_ignore):
    blacklist_embedded = getattr(embedder, handler)([" ".join(terms_to_ignore)])
    return (blacklist_embedded,)


@app.cell
def _(query, re, terms_to_ignore):
    tags = [r.replace("#", "") for r in re.findall(r"#\w+", query.value)]
    query_value = query.value
    for tag in tags:
        query_value = query_value.replace(f"#{tag}", "").strip()
    for term in terms_to_ignore:
        query_value = query_value.replace(f"-{term}", "").strip()
    return query_value, tags


@app.cell
def _(embedder, handler, query_value):
    query_embedded = getattr(embedder, handler)([query_value])
    return (query_embedded,)


@app.cell
def _(blacklist_embedded, cosine_similarity, embeddings, query_embedded):
    similarities = cosine_similarity(embeddings, query_embedded)
    negative_similarities = cosine_similarity(embeddings, blacklist_embedded)
    return negative_similarities, similarities


@app.cell
def _(mo, pd, terms_to_ignore):
    def display_stat(item: pd.Series) -> mo.Html:
        return mo.vstack(
            [
                mo.md(f"[{item['link_name']}]({item['url']})"),
                mo.stat(
                    caption=", ".join(
                        [
                            item["category"],
                            (item["topic"] or ""),
                            (item["section"] or ""),
                        ]
                    ),
                    value=item[
                        "similarity" if not terms_to_ignore else "compound_similarity"
                    ],
                    bordered=True,
                    label=item["url"].split("://")[-1].split("/")[0],
                ),
            ]
        )
    return (display_stat,)


@app.cell
def _(display_stat, mo, pd):
    def display_stat_grid(df: pd.DataFrame, rows: int = 3, cols: int = 3) -> mo.Html:
        index_to_pair = {
            (0, 0): 0,
            (0, 1): 1,
            (0, 2): 2,
            (1, 0): 3,
            (1, 1): 4,
            (1, 2): 5,
            (2, 0): 6,
            (2, 1): 7,
            (2, 2): 8,
        }
        return mo.vstack(
            [
                mo.hstack(
                    [display_stat(df.iloc[index_to_pair[(r, c)]]) for c in range(cols)],
                    justify="center",
                )
                for r in range(rows)
            ],
            justify="center",
        )
    return


@app.cell
def _(datamapplot, mo, pd):
    @mo.cache
    def build_datamapplot(X, df: pd.DataFrame, indices: list[str] | None = None):
        if indices is None:
            indices = list(range(len(X)))
        return datamapplot.create_interactive_plot(
            X[indices],
            df.loc[indices]["section"].fillna("Unlabelled").tolist(),
            df.loc[indices]["topic"].tolist(),
            df.loc[indices]["category"].tolist(),
            hover_text=df.loc[indices]["link_name"],
            title="Data Scientist Hub",
            sub_title="A personal knowledge center built upon a curated (yet opinionated!) collection of links to useful online resources.",
            sub_title_font_size=12,
            enable_search=True,
            search_field="hover_text",
            extra_point_data=df.loc[indices][["url"]],
            on_click="window.open(`{url}`)",
            logo="https://github.com/a-slice-of-py/data-scientist-hub/blob/master/docs/assets/dsh_minimal.png?raw=true",
            logo_width=64,
            darkmode=True,
            selection_handler=datamapplot.selection_handlers.DisplaySample(n_samples=10),
        )
    return (build_datamapplot,)


@app.cell
def _(X, binder, build_datamapplot, df, query_value, search_results):
    dmp = build_datamapplot(
        X,
        df,
        indices=search_results.index[:100]
        if (query_value and binder.value)
        else None,
    )
    return (dmp,)


@app.cell
def _():
    # dmp.save("./dsh_datamapplot.html")
    return


@app.cell
def _(display_stat, mo, query_value, search_results):
    top_results = (
        [display_stat(result) for _, result in search_results.iloc[:10].iterrows()]
        if query_value and search_results["similarity"].max()
        else [mo.md("❌ No result!")]
        if query_value
        else []
    )
    return (top_results,)


@app.cell
def _(mo):
    binder = mo.ui.switch(label="Bind plot")
    return (binder,)


@app.cell
def _(binder, mo, query, selected_model, top_results):
    mo.sidebar(
        [
            query,        
            binder,
            *top_results,
            mo.accordion({"Embedding model": selected_model}),
        ],
        width="25%",
    )
    return


@app.cell
def _(dmp):
    dmp
    return


@app.cell
def _(df, negative_similarities, similarities, tags, terms_to_ignore):
    df["similarity"] = similarities[:, 0]
    df["negative_similarity"] = negative_similarities[:, 0]
    df["compound_similarity"] = df["similarity"] - abs(df["negative_similarity"])
    search_results = df.loc[
        df["category"].apply(
            lambda x: any(t in x.lower().split() for t in tags) if tags else True
        )
        | df["topic"].apply(
            lambda x: any(t in x.lower().split() for t in tags) if tags else True
        )
        | df["section"].apply(
            lambda x: (any(t in x.lower().split() for t in tags) if tags else True)
            if x is not None
            else False
        )
    ].sort_values(
        "similarity" if not terms_to_ignore else "compound_similarity",
        ascending=False,
    )
    return (search_results,)


if __name__ == "__main__":
    app.run()
