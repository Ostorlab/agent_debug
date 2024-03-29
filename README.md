<h1 align="center">Agent Debug</h1>

<p align="center">
<img src="https://img.shields.io/badge/License-Apache_2.0-brightgreen.svg">
<img src="https://img.shields.io/github/languages/top/ostorlab/agent_debug">
<img src="https://img.shields.io/github/stars/ostorlab/agent_debug">
<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
</p>

_Debug is a test agent used to help debug runtimes by logging all messages and important settings._

---

## Usage

Agent Debug can be installed directly from the ostorlab agent store or built from this repository.

 ### Install directly from ostorlab agent store

 ```shell
 ostorlab agent install agent/ostorlab/debug
 ```

You can then run the agent with the following command:
```shell
ostorlab scan run --agent agent/ostorlab/debug ip 8.8.8.8 --follow agent/ostorlab/debug 
```
--follow used to follow the logs of the debug agent

### Build directly from the repository

 1. To build the tsunami agent you need to have [ostorlab](https://pypi.org/project/ostorlab/) installed in your machine.  if you have already installed ostorlab, you can skip this step.

```shell
pip3 install ostorlab
```

 2. Clone this repository.

```shell
git clone https://github.com/Ostorlab/agent_debug.git && cd agent_debug
```

 3. Build the agent image using ostorlab cli.

 ```shell
 ostorlab agent build --file=ostorlab.yaml
 ```
 You can pass the optional flag `--organization` to specify your organisation. The organization is empty by default.

 4. Run the agent using on of the following commands:
	 * If you did not specify an organization when building the image:
	  ```shell
	  ostorlab scan run --agent agent//debug ip 8.8.8.8
	  ```
	 * If you specified an organization when building the image:
	  ```shell
	  ostorlab scan run --agent agent/[ORGANIZATION]/debug ip 8.8.8.8
	  ```


## License
[Apache-2](./LICENSE)
