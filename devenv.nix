{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ pkgs.git pkgs.poetry];

  # https://devenv.sh/scripts/
  scripts.hello.exec = "echo Hello from $GREET";
  scripts.init.exec = ''
    poetry install
  '';

  enterShell = ''
    hello
    git --version
    poetry --version
    export PRE_COMMIT_HOME=$PWD/.pre-commit
    export POETRY_CACHE_DIR=$PWD/.poetry-cache-dir                                                                                       ─╯
  '';
}
