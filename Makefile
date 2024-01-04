## -------------------------------------
## |        Data Scientist Hub         |
## -------------------------------------
## 
## docs-serve
##     locally serve docs
.PHONY: docs-serve
docs-serve:
	export ENABLE_MKDOCS_PLUGIN=false && mkdocs serve
## 
## server-up
##     run server for local development
.PHONY: server-up
server-up:
	docker-compose up server
## 
## run-hooks
##     run pre-commit hooks
.PHONY: run-hooks
run-hooks:
	pre-commit run --all-files
## 
## gource-play
##     shows git history as gource animation
.PHONY: gource-play
gource-play:
	git log --pretty=format:"%at|%s" --reverse --no-merges > gource-caption.txt \
	&& gource --key \
	--user-image-dir 'docs/assets/avatar' \
	--seconds-per-day .5 \
	--auto-skip-seconds 1 \
	--title "DSH Development" \
	--caption-file gource-caption.txt \
	--caption-offset -90 \
	--caption-duration 4 \
	--logo 'docs\assets\dsh_gource.png' \
	--logo-offset 50x1050 -f
## 
## gource-build
##     save git history as gource video
.PHONY: gource-build
gource-build:
	git log --pretty=format:"%at|%s" --reverse --no-merges > gource-caption.txt \
	&& gource --key \
	--user-image-dir 'docs/assets/avatar' \
	--seconds-per-day .5 \
	--auto-skip-seconds 1 \
	--title "DSH Development" \
	--caption-file gource-caption.txt \
	--caption-offset -90 \
	--caption-duration 2 \
	--logo 'docs\assets\dsh_gource.png' \
	--logo-offset 50x1050 -f \
	-o gource.ppm \
	&& ffmpeg \
	-y \
	-r 60 \
	-f image2pipe \
	-vcodec ppm \
	-i gource.ppm \
	-vcodec libx264 \
	-preset ultrafast \
	-pix_fmt yuv420p \
	-crf 17 \
	-threads 0 \
	-bf 0 gource.mp4 \
	&& rm gource.ppm
## 
## mp42gif
##     convert mp4 video to gif
.PHONY: mp42gif
mp42gif:
	ffmpeg -i gource.mp4 -vf "fps=15,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop -1 gource.gif
##  
## help
##     show this help
.PHONY: help
help: Makefile
	@sed -n 's/^## //p' $<