{ pkgs }: {
  deps = [
    pkgs.python39Packages.bootstrapped-pip
    pkgs.python3
    pkgs.python39Packages.flask
  ];
}