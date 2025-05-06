---
date: 2025-03-29
authors:
  - silvio
categories:
  - Announcements
tags:
  - Open Source
---

# Nushell and AWS service reference

Few days ago I discovered [nushell](https://github.com/nushell/nushell) and I immediately fell in love with it.

After some time spent in porting my previous [cmder](https://github.com/cmderdev/cmder) configuration/helpers/backup scripts to nushell, I decided to play around with some nice scripts to help with AWS cloud development routine tasks.

<!-- more -->

The first output is [`nu-aws-service-reference`](https://github.com/a-slice-of-py/nu-aws-service-reference): a Nushell module to interactively browse and discover [AWS Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/service-reference.html).

It has been mentioned in [This week in Nushell](https://www.nushell.sh/blog/2025-03-29-twin0292.html#awesome-nu): cool!

## How it works

This little helper can be used in Nushell as `awssr` and accepts two string parameters (with tab completion!): `service` name (e.g. s3) and `action` name (e.g. ListBucket).

AWS service reference data are obtained programmatically via `http get` as suggested in the [AWS Service Authorization Reference docs](https://docs.aws.amazon.com/service-authorization/latest/reference/service-reference.html).

A table of the in-memory sqlite database is used to cache the list of services and corresponding reference URLs, as suggested in [nushell#12801](https://github.com/nushell/nushell/issues/12801#issuecomment-2676913305).

Each service action list is then served as [completion context](https://www.nushell.sh/book/custom_completions.html#context-aware-custom-completions).

The selected action reference is finally enriched with link to [Permissions](https://aws.permissions.cloud/) and displayed in the terminal.
