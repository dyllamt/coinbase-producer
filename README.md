## Usage

[Helm](https://helm.sh) must be installed to use the charts.  Please refer to
Helm's [documentation](https://helm.sh/docs) to get started.

Once Helm has been set up correctly, add the repo as follows:

  helm repo add <alias> https://dyllamt.github.io/coinbase-connector

If you had already added this repo earlier, run `helm repo update` to retrieve
the latest versions of the packages.  You can then run `helm search repo
<alias>` to see the charts.

To install the coinbase-connector chart:

    helm install my-coinbase-connector <alias>/coinbase-connector

To uninstall the chart:

    helm delete my-coinbase-connector
