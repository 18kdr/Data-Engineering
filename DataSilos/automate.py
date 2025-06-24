import prefect
from prefect import flow, task
from prefect_shell import ShellOperation
import papermill as pm

@task
def executing_notebook():
    pm.execute_notebook(
        "DataSilos.ipynb",
        "Datasilos_Executed.ipynb"
    )

@flow
def executing_notebook_flow():
    result = ShellOperation(
        commands=["pip install -r requirements.txt"]
    ).run()
    executing_notebook()

if __name__ == "__main__":
    executing_notebook_flow()