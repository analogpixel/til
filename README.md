
How I quickly find stuff in this repo via the header:

`alias til='cat /path/to/til/.search | fzf -d "," --with-nth 1 | cat /path/to/til/$(awk -F, {"print \$2"})'`

 ## Affinity
- [Affinity Designer coloring tutorial](til/afinity_designer-vectorize.md)
## Ansible
- [Ansible adhoc command](til/ansible-adhoc-command.md)
- [Ansible console a repl for ansible](til/ansible-console.md)
- [Ansible Dump out all the host inventory](til/ansible-dump-host-inventory.md)
- [Ansible debugger](til/ansible-debugger.md)
## Awk
- [AWK How to clean up logs with Java Stack Traces in them](til/awk-trim-java-stack-trace-logs.md)
- [Awk counting words](til/awk-counting-words.md)
## Azure
- [Azure grow centos disk](til/azure-grow-centos-disk.md)
## Bash
- [Bash cycle through arguments](til/bash-cycle-through-arguments.md)
- [Bash shell vs. environment variables](til/bash-shell-vs-environment-variables.md)
- [Bash test](til/bash-test.md)
- [Bash export yaml var file as environmental variables](til/bash-kubernetes-var-file-export-env.md)
- [Bash last command exit status](til/bash-last-proc-exit-status.md)
- [Bash Yes/No Prompt](til/bash-yes-no-prompt.md)
- [Bash ping test](til/bash-ping-test.md)
- [Bash variable defaults :- vs :=](til/bash-variable-defaults.md)
- [Bash Argument Parser](til/bash-argument-parser.md)
- [Bash run actual command and not alias](til/bash-run-command-not-alias.md)
- [Bash echo no newline](til/bash-echo-no-newline.md)
- [Bash Loop till string is empty](til/bash-loop-untill-empty.md)
- [Bash split string by column separator](til/bash-split-string-column.md)
- [Bash Loop over comma](til/bash-loop-over-comma.md)
## Blender
- [Blender HDRI files](til/blender-hdri-file.md)
## Chezmoi
- [Chezmoi dotfile manager](til/chezmoi-dotfile-manager.md)
## Cli
- [CLI Remote pbcopy (remote data to local clipboard)](til/cli-remote-pbcopy.md)
- [CLI hatop tui for haproxy](til/cli-hatop.md)
- [CLI date format options](til/cli-date-format.md)
## Clojure
- [Clojure reload file in repl](til/clojure-repl-reload-file.md)
- [Clojure working with sequences](til/clojure-sequences.md)
- [Clojure database access sqlite/jdbc](til/clojure-database-access.md)
## Css
- [CSS Selector Reference](til/css-selectors.md)
## Curl
- [Curl resolve hostname to different IP](til/curl-resolve-to-differnt-ip.md)
- [Curl Set Header Values](til/curl-set-headers.md)
## Cut
- [Cut space delimiter work like AWK](til/cut-work-like-awk.md)
## Docker
- [Docker prevent container from exiting](til/docker-prevent-container-from-exiting.md)
- [Docker Build Args](til/docker-builds-args.md)
## Entr
- [Entr reload a program or script on file changes](til/entr-reload-program-on-file-change.md)
## Firefox
- [Firefox extensios](til/firefox-extension.md)
- [Firefox browser.storage.local](til/firefox-browser-storage-local.md)
## Fzf
- [FZF Only display certain columns](til/fzf-only-display-x-col.md)
- [FZF Select multiple items from list in fzf](til/fzf-multiple-from-list.md)
- [FZF Return default value if user exits with esc/ctrl-c](til/fzf-default-value-on-exit.md)
## Git
- [Git remove files from staging  (local commit)](til/git-remove-from-staging.md)
- [Git Detect if you are in git repo](til/git-detect-in-repo.md)
- [GIT revert a file from master](til/git-revert-file-from-master.md)
- [GIT get root directory of repo](til/git-top-level.md)
- [Git Log](til/git-log.md)
## Googlecloud
- [GoogleCloud Logs](til/google-cloud-logs.md)
## Grep
- [Grep show regex matches](til/grep-show-regex-matches.md)
## Java
- [Java check if NaN](til/java-nan.md)
## Javascript
- [Javascript Code Between Imports](til/javascript-code-between-imports.md)
- [Javascript sort numbers](til/javascript-sort-numbers.md)
## Json
- [JSON gron the grepper for json](til/json-gron-cli-utility.md)
## Justfile
- [Justfile a basic example](til/justfile-basic-justfile.md)
## Kind
- [Kind local docker registry](til/kind-local-docker-registry.md)
- [Kind Using your Own docker login with Kind](til/kind-use-docker-login.md)
## Kubectl
- [kubectl forward a port to your local machine](til/kubectl-port-forward.md)
- [Kubectl specify context per command](til/kubectl-context.md)
## Kubernetes
- [kubernetes list all api resources in cluster](til/kubernetes-list-all-api-resources.md)
- [kubernetes Job](til/kubernetes-job.md)
- [Kubernetes load a ssl cert into secrets](til/kubernetes-ssl-cert.md)
- [Kubernetes health probes](til/kubernetes-health-probes.md)
- [Kubernetes explain](til/kubectl-explain.md)
- [kubernetes watch kubectl output](til/kubernetes-watch-kubectl.md)
- [Kubernetes pod placement](til/kubernetes-pod-placement.md)
- [Kubernetes pod life cycle start/stop hooks](til/kubernetes-life-cycle.md)
- [kubernetes host aliases (/etc/hosts)](til/kubernetes-host-aliases.md)
## Linux
- [Linux stop respawning initd service](til/linux-stop-respawning-initd-service.md)
## Macos
- [Macos hide all windows](til/macos-hide-all-windows.md)
- [Macos Font smoothing](til/macos-font-smoothing.md)
- [Macos find process listening on port](til/macos-find-listening-port.md)
## Math
- [Math Properties of Exponents](til/math-properties-of-exponents.md)
## Misc
- [Misc How to Unsubscribe from ...](til/misc-unsubscribe-from.md)
- [Misc Vesa Mounting Standards](til/misc-vesa-mounting-standards.md)
## Nmap
- [NMAP scripts](til/nmap-scripts.md)
## Openssl
- [Openssl create signing cert (csr)](til/openssl-create-csr.md)
- [openssl inspect cert](til/openssl-inspect-cert.md)
## P5.js
- [P5.js dynamic mask](til/p5js-dynamic-mask.md)
## Packer
- [Packer in a docker container](til/ssh_auth_in_docker_container.md)
## Pgrep
- [Pgrep character Limit](til/pgrep-character-limit.md)
## Prometheus
- [prometheus promql count change in value](til/prometheus-change-in-value.md)
- [Prometheus alertmanager send test alert](til/prometheus-alertmanager-send-test.md)
## Prometheus-operator
- [Prometheus-operator Pod Monitors vs. Service Monitors](til/kubernetes_operator-podmonitor-vs-servicemonitor.md)
## Python
- [Python convert case](til/python-convert-case.md)
- [Python a functional decimal to hex conversion](til/python-decimal-to-hex.md)
- [Python webserver mode](til/python-web-server.md)
- [Python logging](til/python-logging.md)
- [Python functional programming](til/python-functional-programming.md)
- [Python Dictionary Comprehension](til/python-dictionary-comprehension.md)
- [Python enumerate indexed foreach](til/python-enumerate-indexed-foreach.md)
- [Python Install jupyterhub](til/python-jupyerhub-install.md)
- [Python bitwise operators](til/python-bitwise-operators.md)
- [Python Change working directory (cwd)](til/python-change-working-directory.md)
- [Python working with CSV files](til/python-csv-files.md)
- [Python define required modules to install from file](til/python-modules-requirementstxt.md)
- [Python expand tilde in path](til/python-expand-unix-path.md)
- [Python Date and Time](til/python-date-time.md)
- [Python Load Variables from Environmental Variables](til/python-load-vars-from-environ-vars.md)
- [Python set theory](til/python-set-theory.md)
- [Python Add or Update to a list in a dict](til/python-add_update_list_in_dict.md)
- [Python remove non-characters from string](til/python-remove-non-alpha-characters.md)
- [Python Sqlite](til/python-sqlite.md)
- [Python Assignment in Expression (assign variable in if condition)](til/python-assignment-in-expression.md)
- [Python Converting a list to a dict](til/python-dict-from-list.md)
## Raspberry
- [Raspberry Pi Disable Wifi](til/raspberrypi-disable-wifi.md)
## Raspberrypi
- [RaspberryPi firefox](til/raspberrypi-firefox.md)
## Raspberypi
- [RaspberyPi automount usb drives](til/raspberrypi-automount-volume.md)
## Rclone
- [Rclone mount cloud drives](til/rclone-mount-cloud-drives.md)
## Rpm
- [RPM Fix Corrupt database](til/rpm-fix-corrupt-database.md)
## Ruby
- [Ruby in juptyer notebooks](til/ruby-jupyter-notebook.md)
## Sqlite
- [Sqlite csv query](til/sqlite-csv-query.md)
## Ssh
- [SSH Debugging a conneciton](til/ssh-debug-connection.md)
## Systemd
- [Systemd clean up journalctl logs](til/systemd-cleanup-journalctl-logs.md)
- [Systemd Debug tmp cleaner](til/systemd-debug-tmp-cleaner.md)
- [Systemd basic unit service](til/systemd-basic-unit-service.md)
## Tello
- [Tello change wifi mode](til/tello-change-wifi-mode.md)
## Vim
- [Vim Tabs](til/vim-tabs.md)
- [Vim Jump to your last change](til/vim-jump-to-last-change.md)
- [Vim Sessions](til/vim-sessions.md)
- [Vim Ignore Case](til/vim-ignore-case.md)
- [Vim clipboard history](til/vim-clipboard-history.md)
## Wikidata
- [Wikidata query](til/wikidata-query.md)
## X
- [X rotate the screen](til/x-rotate-screen.md)
- [X remap caps lock to ctrl](til/x-remap-caps-key.md)
## Zookeeper
- [Zookeeper Check if alive](til/zookepper-check-alive.md)
---
