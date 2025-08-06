from invoke import task
#
# when invoking tasks remember that the dashes "_" are replaced by hyphens "-" on the command line.
#


@task
def build_e_divisive(c):
    c.run("poetry run compile-ext")

@task(build_e_divisive)
def build(c):
    c.run("poetry build")
    c.run("poetry run pytest")

@task
def pytests(c):
    c.run("poetry run pytest")

@task()
def test_python_version(c, version):
    c.run(f"poetry env use {version}")
    c.run("poetry update")
    c.run("poetry run pytest")

@task
def clean(c):
    c.run("rm -rf build/*")
    c.run("rm -rf dist/*")
    c.run("rm -rf otava/signal_processing_algorithms/e_divisive/calculators/_e_divisive*.so")

