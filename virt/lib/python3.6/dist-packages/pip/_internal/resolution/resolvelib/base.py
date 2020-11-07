from pip._vendor.packaging.specifiers import SpecifierSet
from pip._vendor.packaging.utils import canonicalize_name

from pip._internal.req.req_install import InstallRequirement
from pip._internal.utils.hashes import Hashes
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import FrozenSet, Iterable, Optional, Tuple

    from pip._vendor.packaging.version import _BaseVersion

    from pip._internal.models.link import Link

    CandidateLookup = Tuple[
        Optional["Candidate"],
        Optional[InstallRequirement],
    ]


def format_name(project, extras):
    # type: (str, FrozenSet[str]) -> str
    if not extras:
        return project
    canonical_extras = sorted(canonicalize_name(e) for e in extras)
    return "{}[{}]".format(project, ",".join(canonical_extras))


class Constraint(object):
    def __init__(self, specifier, hashes):
        # type: (SpecifierSet, Hashes) -> None
        self.specifier = specifier
        self.hashes = hashes

    @classmethod
    def empty(cls):
        # type: () -> Constraint
        return Constraint(SpecifierSet(), Hashes())

    @classmethod
    def from_ireq(cls, ireq):
        # type: (InstallRequirement) -> Constraint
        return Constraint(ireq.specifier, ireq.hashes(trust_internet=False))

    def __nonzero__(self):
        # type: () -> bool
        return bool(self.specifier) or bool(self.hashes)

    def __bool__(self):
        # type: () -> bool
        return self.__nonzero__()

    def __and__(self, other):
        # type: (InstallRequirement) -> Constraint
        if not isinstance(other, InstallRequirement):
            return NotImplemented
        specifier = self.specifier & other.specifier
        hashes = self.hashes & other.hashes(trust_internet=False)
        return Constraint(specifier, hashes)


class Requirement(object):
    @property
    def name(self):
        # type: () -> str
        raise NotImplementedError("Subclass should override")

    def is_satisfied_by(self, candidate):
        # type: (Candidate) -> bool
        return False

    def get_candidate_lookup(self):
        # type: () -> CandidateLookup
        raise NotImplementedError("Subclass should override")

    def format_for_error(self):
        # type: () -> str
        raise NotImplementedError("Subclass should override")


class Candidate(object):
    @property
    def name(self):
        # type: () -> str
        raise NotImplementedError("Override in subclass")

    @property
    def version(self):
        # type: () -> _BaseVersion
        raise NotImplementedError("Override in subclass")

    @property
    def is_installed(self):
        # type: () -> bool
        raise NotImplementedError("Override in subclass")

    @property
    def is_editable(self):
        # type: () -> bool
        raise NotImplementedError("Override in subclass")

    @property
    def source_link(self):
        # type: () -> Optional[Link]
        raise NotImplementedError("Override in subclass")

    def iter_dependencies(self, with_requires):
        # type: (bool) -> Iterable[Optional[Requirement]]
        raise NotImplementedError("Override in subclass")

    def get_install_requirement(self):
        # type: () -> Optional[InstallRequirement]
        raise NotImplementedError("Override in subclass")

    def format_for_error(self):
        # type: () -> str
        raise NotImplementedError("Subclass should override")
