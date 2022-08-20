# version_info = (0, 4, 0, "final")
# This is a temporary work around for the strict requirement of jupyter-book's (~0.13) dependencies.
version_info = (0, 3, 2, "final")

_specifier_ = {"alpha": "a", "beta": "b", "candidate": "rc", "final": ""}

__version__ = "{}.{}.{}{}".format(
    version_info[0],
    version_info[1],
    version_info[2],
    ""
    if version_info[3] == "final"
    else _specifier_[version_info[3]] + str(version_info[4]),
)
