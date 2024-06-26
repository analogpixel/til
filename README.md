
How I quickly find stuff in this repo via the header:

`alias til='cat /path/to/til/.search | fzf -d "," --with-nth 1 | cat /path/to/til/$(awk -F, {"print \$2"})'`

 ## Add
- [Add (calculate on) a file of numbers ( paste: bash version of join )](til/bash-paste-add-file-of-numbers.md)
## Affinity
- [Affinity Designer coloring tutorial](til/afinity_designer-vectorize.md)
## Ansible
- [Ansible load a variable dynamically from another host](til/ansible-load-var-from-another-host.md)
- [Ansible adhoc command](til/ansible-adhoc-command.md)
- [Ansible Debugging](til/ansible-debugging.md)
- [Ansible console a repl for ansible](til/ansible-console.md)
- [Ansible Constructed Inventories (dynamic)](til/ansible-constructed-inventories.md)
- [Ansible template task to run a role](til/ansible-template-task-role.md)
- [Ansible omit/remove module parameter if variable is null](til/ansible-omit-variable-options.md)
- [Ansible Run Task From Role](til/ansible-run-task-from-role.md)
- [Ansible backup files](til/ansible-backup-files.md)
- [Ansible create a random password](til/ansible-create-random-password.md)
- [Ansible Dump out all the host inventory](til/ansible-dump-host-inventory.md)
- [Ansible debugger](til/ansible-debugger.md)
- [Ansible Dry Run (check)](til/ansible-dry-run.md)
- [Ansible append to a fact](til/ansible-append-to-fact.md)
- [Ansible display rendered inventory](til/ansible-display-rendered-inventory.md)
## Atuin
- [atuin sqlite shell history](til/bash-atuin.md)
## Awk
- [AWK How to clean up logs with Java Stack Traces in them](til/awk-trim-java-stack-trace-logs.md)
- [Awk counting words](til/awk-counting-words.md)
- [Awk random number in range](til/awk-random-range.md)
## Azure
- [Azure grow centos disk](til/azure-grow-centos-disk.md)
## Bash
- [Bash cycle through arguments](til/bash-cycle-through-arguments.md)
- [Bash shell vs. environment variables](til/bash-shell-vs-environment-variables.md)
- [Bash test](til/bash-test.md)
- [Bash export yaml var file as environmental variables](til/bash-kubernetes-var-file-export-env.md)
- [Bash creating gifs with ffmpeg and gifsicle](til/bash-creating-gifs.md)
- [Bash create a temporary file handle that can be passed as input to another command](til/bash-command-to-filehandle.md)
- [Bash last command exit status](til/bash-last-proc-exit-status.md)
- [Bash Yes/No Prompt](til/bash-yes-no-prompt.md)
- [Bash range expansion with xargs and ssh](til/bash-range-expansion-ssh.md)
- [Bash check if ip is in subnet range](til/bash-check-ip-in-range.md)
- [Bash ping test](til/bash-ping-test.md)
- [Bash variable defaults :- vs :=](til/bash-variable-defaults.md)
- [Bash Argument Parser](til/bash-argument-parser.md)
- [Bash loop over lines and get columns](til/bash-loop-lines.md)
- [Bash Case statement](til/bash-case-statement.md)
- [Bash Lock File with Flock](til/bash-lockfile-with-flock.md)
- [Bash run actual command and not alias](til/bash-run-command-not-alias.md)
- [Bash replace a block of text](til/bash-replace-block-of-text.md)
- [Bash echo no newline](til/bash-echo-no-newline.md)
- [Bash Loop till string is empty](til/bash-loop-untill-empty.md)
- [Bash loop over command output](til/bash-loop-command-output.md)
- [Bash pause/stop output](til/bash-pause-output.md)
- [Bash view markdown in the terminal](til/bash-terminal-markdown.md)
- [Bash split string by column separator](til/bash-split-string-column.md)
- [Bash Loop over comma](til/bash-loop-over-comma.md)
- [Bash Convert CSV list to JSON array](til/bash-csv-list-to-json-array.md)
## Blender
- [Blender HDRI files](til/blender-hdri-file.md)
## Chezmoi
- [Chezmoi dotfile manager](til/chezmoi-dotfile-manager.md)
## Cli
- [CLI Remote pbcopy (remote data to local clipboard)](til/cli-remote-pbcopy.md)
- [CLI hatop tui for haproxy](til/cli-hatop.md)
- [CLI subnet calculator](til/cli-subnet-calculator.md)
- [CLI date format options](til/cli-date-format.md)
## Clojure
- [Clojure reload file in repl](til/clojure-repl-reload-file.md)
- [Clojure working with sequences](til/clojure-sequences.md)
- [Clojure database access sqlite/jdbc](til/clojure-database-access.md)
## Comm,
- [comm, select or reject lines common to two files](til/bash-comm.md)
## Css
- [CSS Selector Reference](til/css-selectors.md)
## Curl
- [Curl connect to ldap](til/curl-connect-to-ldap.md)
- [Curl sending emails](til/curl-send-mail.md)
- [Curl resolve hostname to different IP](til/curl-resolve-to-differnt-ip.md)
- [Curl Set Header Values](til/curl-set-headers.md)
## Cut
- [Cut space delimiter work like AWK](til/cut-work-like-awk.md)
## Docker
- [Docker prevent container from exiting](til/docker-prevent-container-from-exiting.md)
- [Docker Build Args](til/docker-builds-args.md)
## Editing
- [Editing Guitar Tabs in Vim](til/vim-edit-guitar-tabs.md)
## Entr
- [Entr reload a program or script on file changes](til/entr-reload-program-on-file-change.md)
## Exercism
- [Exercism download all from track](til/exercism-download-all.md)
## Firefox
- [Firefox extensios](til/firefox-extension.md)
- [Firefox reduce motion setting](til/firfox-reduce-motion.md)
- [Firefox browser.storage.local](til/firefox-browser-storage-local.md)
## Flask
- [Flask Console Output in kubernetes with python](til/flask-console-output.md)
## Fzf
- [FZF Only display certain columns](til/fzf-only-display-x-col.md)
- [FZF Select multiple items from list in fzf](til/fzf-multiple-from-list.md)
- [FZF Return default value if user exits with esc/ctrl-c](til/fzf-default-value-on-exit.md)
- [FZF show ansi colors](til/fzf-show-ansi-colors.md)
## Gcloud
- [gcloud check is oslogin is enabled.](til/gcloud-oslogin-enabled.md)
- [gcloud container registry list images filter by tag name](til/gcloud-filter-tags.md)
## Get
- [Get password from onepassword in python](til/python-onepassword.md)
## Git
- [Git remove files from staging  (local commit)](til/git-remove-from-staging.md)
- [Git Detect if you are in git repo](til/git-detect-in-repo.md)
- [GIT revert a file from master](til/git-revert-file-from-master.md)
- [git reset your master](til/git-reset-master.md)
- [GIT get root directory of repo](til/git-top-level.md)
- [Git Log](til/git-log.md)
## Google
- [Google Cloud Auth to Docker Registry](til/google-cloud-auth-docker.md)
## Googlecloud
- [GoogleCloud Logs](til/google-cloud-logs.md)
## Grafana
- [Grafana show all annotations](til/grafana-show-all-annotations.md)
## Grep
- [Grep show regex matches](til/grep-show-regex-matches.md)
## Http
- [http x-forwarded-host redirection](til/networking-x-forwarded-host.md)
## Iterm2
- [ITerm2 duplicate tab](til/iterm-duplicate-tab.md)
## Java
- [Java check if NaN](til/java-nan.md)
- [Java running a heap dump](til/java-heap-dump.md)
## Javascript
- [Javascript seconds since epoch](til/javascript-seconds-since-epoc.md)
- [Javascript Code Between Imports](til/javascript-code-between-imports.md)
- [Javascript sort numbers](til/javascript-sort-numbers.md)
## Jq
- [JQ examples](til/jq-examples.md)
- [JQ object expansion](til/jq-object-expand.md)
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
- [kubectl labels and selectors](til/kubectl-labels-and-selectors.md)
- [Kubectl mc (multicluster search)](til/kubectl-mc.md)
## Kubernetes
- [kubernetes list all api resources in cluster](til/kubernetes-list-all-api-resources.md)
- [kubernetes list cluster versions](til/kubectl-list-cluster-versions.md)
- [Kubernetes service and pod dns names](til/kubernetes-service-and-pod-dns.md)
- [kubernetes diff 2 manifest files](til/kubernetes-diff-manifests.md)
- [kubernetes roll out new image](til/kubernetes-roll-out-new-image.md)
- [kubernetes get all objects in a namespace](til/kubernetes-get-all-objects-in-namespace.md)
- [kubernetes Job](til/kubernetes-job.md)
- [Kubernetes load a ssl cert into secrets](til/kubernetes-ssl-cert.md)
- [Kubernetes health probes](til/kubernetes-health-probes.md)
- [Kubernetes explain](til/kubectl-explain.md)
- [kubernetes mount single file with subpath](til/kubernetes-volume-subpath.md)
- [kubernetes watch kubectl output](til/kubernetes-watch-kubectl.md)
- [kubernetes changelogs](til/kubernetes-changelogs.md)
- [Kubernetes pod placement](til/kubernetes-pod-placement.md)
- [Kubernetes pod life cycle start/stop hooks](til/kubernetes-life-cycle.md)
- [kubernetes host aliases (/etc/hosts)](til/kubernetes-host-aliases.md)
## Linux
- [Linux stop respawning initd service](til/linux-stop-respawning-initd-service.md)
## Macos
- [Macos plaintext paste by default](til/macos-disable-paste-formatting.md)
- [Macos hide all windows](til/macos-hide-all-windows.md)
- [Macos Font smoothing](til/macos-font-smoothing.md)
- [Macos disable apple music from starting](til/macos-disable-apple-music.md)
- [Macos find process listening on port](til/macos-find-listening-port.md)
## Math
- [Math polar to cartesian](til/math-polar-to-caresian.md)
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
- [P5.JS perfect gif loop](til/p5js-perfect-gif-loop.md)
- [P5.js dynamic mask](til/p5js-dynamic-mask.md)
- [P5.js set size to window size](til/p5js-set-size-of-window.md)
## Packer
- [Packer in a docker container](til/ssh_auth_in_docker_container.md)
## Pgrep
- [Pgrep character Limit](til/pgrep-character-limit.md)
## Prometheus
- [prometheus promql count change in value](til/prometheus-change-in-value.md)
- [prometheus operator blackbox probes](til/prometheus-operator-blackbox-probes.md)
- [Prometheus alertmanager send test alert](til/prometheus-alertmanager-send-test.md)
## Prometheus-operator
- [Prometheus-operator Pod Monitors vs. Service Monitors](til/kubernetes_operator-podmonitor-vs-servicemonitor.md)
## Python
- [Python custom sort comparator](til/python-custom-comparator.md)
- [Python play a sound in macos](til/python-play-sound-macos.md)
- [Python environment boolean variable](til/python-environmental-booleans.md)
- [Python convert case](til/python-convert-case.md)
- [Python Overriding __init__](til/python-override-init.md)
- [Python a functional decimal to hex conversion](til/python-decimal-to-hex.md)
- [Python dataclasses (c like struct)](til/python-struct-dataclass.md)
- [Python webserver mode](til/python-web-server.md)
- [Python logging](til/python-logging.md)
- [Python functional programming](til/python-functional-programming.md)
- [Python Dictionary Comprehension](til/python-dictionary-comprehension.md)
- [Python enumerate indexed foreach](til/python-enumerate-indexed-foreach.md)
- [Python return value when list is empty during pop](til/python-pop-empty-value.md)
- [Python Install jupyterhub](til/python-jupyerhub-install.md)
- [Python bitwise operators](til/python-bitwise-operators.md)
- [Python Change working directory (cwd)](til/python-change-working-directory.md)
- [Python working with CSV files](til/python-csv-files.md)
- [Python pretty print a dict/hash](til/python-pretty-print-dict.md)
- [Python run a command and get the output](til/python-run-a-command.md)
- [Python read in a matrix](til/python-read-in-matrix.md)
- [Python define required modules to install from file](til/python-modules-requirementstxt.md)
- [Python expand tilde in path](til/python-expand-unix-path.md)
- [Python Date and Time](til/python-date-time.md)
- [Python get nested JSON/dict key from path](til/python-json-key.md)
- [Python create a directory (create parents)](til/python-create-a-directory.md)
- [Python print string unformatted](til/python-print-unformatted.md)
- [Python Load Variables from Environmental Variables](til/python-load-vars-from-environ-vars.md)
- [Python set theory](til/python-set-theory.md)
- [Python Add or Update to a list in a dict](til/python-add_update_list_in_dict.md)
- [Python cli template](til/python-cli-template.md)
- [Python remove non-characters from string](til/python-remove-non-alpha-characters.md)
- [Python Sqlite](til/python-sqlite.md)
- [Python Assignment in Expression (assign variable in if condition) The walrus operator :=](til/python-assignment-in-expression.md)
- [Python socks proxy support](til/python-socks-proxy.md)
- [Python Converting a list to a dict](til/python-dict-from-list.md)
- [Python format a string (fstring)](til/python-format-string.md)
## Raspberry
- [Raspberry Pi Disable Wifi](til/raspberrypi-disable-wifi.md)
## Raspberrypi
- [RaspberryPi firefox](til/raspberrypi-firefox.md)
## Raspberypi
- [RaspberyPi automount usb drives](til/raspberrypi-automount-volume.md)
## Rclone
- [Rclone mount cloud drives](til/rclone-mount-cloud-drives.md)
## Regex
- [Regex named character sets](til/regex-named-characters-sets.md)
## Rpm
- [RPM Fix Corrupt database](til/rpm-fix-corrupt-database.md)
## Rsa
- [RSA convert exponent modulus to regular private key format](til/rsa-convert-exponent-modulus.md)
## Ruby
- [Ruby in juptyer notebooks](til/ruby-jupyter-notebook.md)
## Rust
- [Rust debug print a variable](til/rust-debug-print.md)
## Sending
- [Sending a message to google chat in curl](til/googlechat-send-message.md)
## Slack
- [Slack bolt python ack a message](til/slack-bolt-ack-message.md)
## Sql
- [SQL replace null values](til/sql-replace-null-values.md)
## Sqlite
- [Sqlite csv query](til/sqlite-csv-query.md)
## Ssh
- [SSH Debugging a conneciton](til/ssh-debug-connection.md)
- [SSH socks proxy server](til/ssh-socks-proxy.md)
## Systemd
- [Systemd clean up journalctl logs](til/systemd-cleanup-journalctl-logs.md)
- [Systemd Debug tmp cleaner](til/systemd-debug-tmp-cleaner.md)
- [Systemd basic unit service](til/systemd-basic-unit-service.md)
## Tcpdump
- [TCPDUMP examples](til/tcpdump-examples.md)
## Tello
- [Tello change wifi mode](til/tello-change-wifi-mode.md)
## Tools
- [tools for working with jupyer notebooks from the cli](til/python-nbcommands.md)
## Vim
- [Vim Tabs](til/vim-tabs.md)
- [Vim add to openwith in macos](til/vim-add-to-openwith-macos.md)
- [Vim Jump to your last change](til/vim-jump-to-last-change.md)
- [Vim wrap text at 80 characters](til/vim-wrap-at-80.md)
- [Vim Sessions](til/vim-sessions.md)
- [Vim Ignore Case](til/vim-ignore-case.md)
- [Vim clipboard history](til/vim-clipboard-history.md)
## Wikidata
- [Wikidata query](til/wikidata-query.md)
## X
- [X rotate the screen](til/x-rotate-screen.md)
- [X remap caps lock to ctrl](til/x-remap-caps-key.md)
## Yaml
- [yaml anchors](til/yaml-anchors.md)
## Zookeeper
- [Zookeeper Check if alive](til/zookepper-check-alive.md)
---
