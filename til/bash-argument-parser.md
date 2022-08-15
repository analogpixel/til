# Bash Argument Parser

A bash argument parser that supports short options, long options, or 
positional arguments as well.

```bash

POSITIONAL_ARGS=()
main() {
  while [[ "$#" > 0 ]]; do
    arg="$1"
    shift
    case "${arg}" in
      -d|--debug)
        local -r debug=yes
        ;;

      -h|--help|help)
        help_text
        exit 0
        ;;
      -*|--*)
        echo "Unknown option $1"
        exit 1
        ;;
      *)
        POSITIONAL_ARGS+=("$arg") # save positional arg
        echo "got one"
        ;;
    esac
  done

  set -- "${POSITIONAL_ARGS[@]}" # restore positional parameters $1 $2...etc

  if [[ ${#POSITIONAL_ARGS[@]} != 2  ]]  ; then
    echo "Requires 2 servers"
    echo ${#POSITIONAL_ARGS[@]}
    exit
  fi


```
