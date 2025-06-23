import prefect
from prefect import flow, task
import papermill as pm

@task
def executing_notebook():
    pm.execute_notebook(
        "DataSilos.ipynb",
        "Datasilos_Executed.ipynb"
    )

@flow
def executing_notebook_flow():
    executing_notebook()

if __name__ == "__main__":
    executing_notebook_flow()