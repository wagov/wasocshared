"""Shared helpers for the WA SOC guidance site."""


def define_env(env):
    """Register MkDocs macros from the package macro module."""
    from .macros import define_env as register_macros

    return register_macros(env)
