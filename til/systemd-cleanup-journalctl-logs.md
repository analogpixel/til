# Systemd clean up journalctl logs

you can cleanup systemd journal logs either by size, or time:

## clean up logs until you get to 500meg
`journalctl --vacuum-size=500M`

## clean up logs that are older than 2 days
`journalctl --vacuum-time=2d`
