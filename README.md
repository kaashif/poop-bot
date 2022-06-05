# poop-bot
Program that cheats (or rather, plays very well) this game: https://python-vs-poop.anvil.app/

## How to run

These are instructions mainly so I don't forget how to run my own script. They may be slightly
inaccurate and are only intended as a vague guide.

Install Docker. Then run:

```
$ docker run -it -v $(pwd):/data --rm --ipc=host mcr.microsoft.com/playwright/python:v1.22.0-focal /bin/bash
```

and in the container, run `async.py` or `sync.py`.

The Docker container is because installing Playwright when not on Ubuntu is rather painful, and I'm on Debian.

To view a video, uncomment the line that adds the `record_video_dir` to the browser context.

## License

MIT license, read `LICENSE` for more.