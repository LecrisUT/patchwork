from __future__ import print_function
from importlib import import_module

from invocations import docs
from invocations.checks import blacken
from invocations.packaging import release
from invocations.pytest import test, coverage

from invoke import Collection, task


@task
def sanity(c):
    """
    Quick sanity check to ensure we're installed successfully. Mostly for CI.
    """
    # Doesn't need to literally import everything, but "a handful" will do.
    for name in ("environment", "files", "transfers"):
        mod = "patchwork.{name}".format(name=name)
        import_module(mod)
        print("Imported {mod} successfully".format(mod=mod))


ns = Collection(docs, release, test, coverage, sanity, blacken)
ns.configure(
    {
        "packaging": {
            "sign": True,
            "wheel": True,
            "check_desc": True,
            "changelog_file": "docs/changelog.rst",
        }
    }
)
