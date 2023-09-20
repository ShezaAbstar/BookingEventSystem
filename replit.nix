{ pkgs }: {
  deps = [
    pkgs.python38Packages.bootstrapped-pip
    pkgs.python3
    pkgs.python39Packages.flask
  ];
}