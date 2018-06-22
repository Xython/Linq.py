from typing import Generic, TypeVar, Iterable, Callable, overload, List, Tuple, Set, Dict, Any, Mapping, Optional

TE = TypeVar('TE')
TE1 = TypeVar('TE1')
TE2 = TypeVar('TE2')
TE3 = TypeVar('TE3')
TE4 = TypeVar('TE4')
TS = TypeVar('TS')

TV = TypeVar('TV')
TK = TypeVar('TK')

RE = TypeVar('RE')
RV = TypeVar('RV')
RK = TypeVar('RK')

U = TypeVar('U')
G = TypeVar('G')
K1 = TypeVar('K1')
K2 = TypeVar('K2')
K3 = TypeVar('K3')
V1 = TypeVar('V1')
V2 = TypeVar('V2')
V3 = TypeVar('V3')
V4 = TypeVar('V4')

R = TypeVar('R', Iterable[RE], Mapping[RK, RV])
T = TypeVar('T', Iterable[TE], Mapping[TK, TV], Iterable[Tuple[TE1, TE2]], Iterable[Tuple[TE1, TE2, TE3, TE4]], TS)


def extension_std(func: function) -> function: ...


def extension_class(cls) -> Callable[[function], function]: ...


def unbox_if_flow(self): ...


class Flow(Generic[T]):
    _e: T

    @property
    def _(self):
        return self._e

    @overload
    def __new__(cls, value: Mapping[TK, TV]) -> Flow[Mapping[TK, TV]]: ...

    @overload
    def __new__(cls, value: Iterable[TE]) -> Flow[Iterable[TE]]: ...

    @overload
    def __new__(cls, value: TS) -> Flow[TS]: ...

    @overload
    def sum(self: Flow[Iterable[int]]) -> Flow[int]: ...

    @overload
    def sum(self: Flow[Iterable[int]], f: Callable[[int], U]) -> Flow[U]: ...

    @overload
    def sum(self: Flow[Iterable[float]]) -> Flow[float]: ...

    @overload
    def sum(self: Flow[Iterable[float]], f: Callable[[float], U]) -> Flow[U]: ...

    def enum(self) -> Flow[Iterable[Tuple[int, TE]]]: ...

    @overload
    def map(self, f: Callable[[TE], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[TE1, TE2], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[Tuple[TE1, TE2]], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[TE1, TE2, TE3], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[Tuple[TE1, TE2, TE3]], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[TE1, TE2, TE3, TE4], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[Tuple[TE1, TE2, TE3, TE4]], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[TK, TK], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def map(self, f: Callable[[Tuple[TK, TV]], RE]) -> Flow[Iterable[RE]]: ...

    @overload
    def then(self, f: Callable[[Mapping[TK, TV]], R]) -> Flow[R]: ...

    @overload
    def then(self, f: Callable[Iterable[TE], R]) -> Flow[R]: ...

    @overload
    def scan(self, f: Callable[[R, TE], R], start_elem: R) -> Flow[Iterable[R]]: ...

    @overload
    def reduce(self, f: Callable[[R, TE], R], start_elem: Optional[R] = None) -> Flow[R]: ...

    @overload
    def filter(self) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[TE], bool]) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[TE1, TE2], bool]) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[Tuple[TE1, TE2]], bool]) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[TE1, TE2, TE3], bool]) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[Tuple[TE1, TE2, TE3]], bool]) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[TE1, TE2, TE3, TE4], bool]) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[Tuple[TE1, TE2, TE3, TE4]], bool]) -> Flow[T]: ...

    @overload
    def filter(self, f: Callable[[TK, TV], bool]) -> Flow[Iterable[Tuple[TK, TV]]]: ...

    @overload
    def filter(self, f: Callable[[Tuple[TK, TV]], bool]) -> Flow[Iterable[Tuple[TK, TV]]]: ...

    @overload
    def each(self, f: Callable[[TK, TV], Any]) -> None: ...

    @overload
    def each(self, f: Callable[[TE], Any]) -> None: ...

    @overload
    def each(self, f: Callable[[TE1, TE2], Any]) -> None: ...

    @overload
    def each(self, f: Callable[[TE1, TE2, TE3], Any]) -> None: ...

    @overload
    def each(self, f: Callable[[TE1, TE2, TE3, TE4], Any]) -> None: ...

    @overload
    def aggregate(self, fn1: Callable[[T], V1], fn2: Callable[[T], V2]) -> Flow[Tuple[V1, V2]]: ...

    @overload
    def aggregate(self, fn1: Callable[[T], V1], fn2: Callable[[T], V2], fn3: Callable[[T], V3]) -> Flow[
        Tuple[V1, V2, V3]]: ...

    @overload
    def aggregate(self, fn1: Callable[[T], V1], fn2: Callable[[T], V2], fn3: Callable[[T], V3],
                  fn4: Callable[[T], V4]) -> Flow[Tuple[V1, V2, V3, V4]]: ...

    @overload
    def aggregate(self, *functions: Callable[[T], R]) -> Flow[Tuple[R, ...]]: ...

    @overload
    def zip(self, others: Iterable[V1]) -> Flow[Iterable[Tuple[TE, V1]]]: ...

    @overload
    def zip(self, others: Flow[Iterable[V1]]) -> Flow[Iterable[Tuple[TE, V1]]]: ...

    @overload
    def zip(self, others1: Iterable[V1], other2: Iterable[V2]) -> Flow[Iterable[Tuple[TE, V1, V2]]]: ...

    @overload
    def zip(self, others1: Flow[Iterable[V1]], other2: Iterable[V2]) -> Flow[Iterable[Tuple[TE, V1, V2]]]: ...

    @overload
    def zip(self, others1: Iterable[V1], other2: Flow[Iterable[V2]]) -> Flow[Iterable[Tuple[TE, V1, V2]]]: ...

    @overload
    def zip(self, others1: Flow[Iterable[V1]], other2: Flow[Iterable[V2]]) -> Flow[Iterable[Tuple[TE, V1, V2]]]: ...

    @overload
    def sorted(self) -> Flow[T]: ...

    @overload
    def sorted(self, by: Callable[[TE], R]) -> Flow[T]: ...

    @overload
    def sorted(self, by: Callable[[TE1, TE2], R]) -> Flow[T]: ...

    @overload
    def sorted(self, by: Callable[[TE1, TE2, TE3], R]) -> Flow[T]: ...

    @overload
    def sorted(self, by: Callable[[TE1, TE2, TE3, TE4], R]) -> Flow[T]: ...

    @overload
    def chunk_by(self) -> Flow[Iterable[Tuple[TE, List[TE]]]]: ...

    @overload
    def chunk_by(self, by: Callable[[TE], R]) -> Flow[Iterable[Tuple[R, List[TE]]]]: ...

    @overload
    def chunk_by(self, by: Callable[[TE1, TE2], R]) -> Flow[Iterable[Tuple[R, List[Tuple[TE1, TE2]]]]]: ...

    @overload
    def chunk_by(self, by: Callable[[TE1, TE2, TE3], R]) -> Flow[Iterable[Tuple[R, List[Tuple[TE1, TE2, TE3]]]]]: ...

    @overload
    def chunk_by(self, by: Callable[[TE1, TE2, TE3, TE4], R]) -> Flow[
        Iterable[Tuple[R, List[Tuple[TE1, TE2, TE3, TE4]]]]]: ...

    @overload
    def chunk_by(self, by: Callable[[Tuple[TE1, TE2]], R]) -> Flow[Iterable[Tuple[R, List[Tuple[TE1, TE2]]]]]: ...

    @overload
    def chunk_by(self, by: Callable[[Tuple[TE1, TE2, TE3]], R]) -> Flow[
        Iterable[Tuple[R, List[Tuple[TE1, TE2, TE3]]]]]: ...

    @overload
    def chunk_by(self, by: Callable[[Tuple[TE1, TE2, TE3, TE4]], R]) -> Flow[
        Iterable[Tuple[R, List[Tuple[TE1, TE2, TE3, TE4]]]]]: ...

    @overload
    def group_by(self) -> Flow[Iterable[Dict[TE, List[TE]]]]: ...

    @overload
    def group_by(self, by: Callable[[TE], R]) -> Flow[Iterable[Dict[R, List[TE]]]]: ...

    @overload
    def group_by(self, by: Callable[[TE1, TE2], R]) -> Flow[Iterable[Dict[R, List[Tuple[TE1, TE2]]]]]: ...

    @overload
    def group_by(self, by: Callable[[Tuple[TE1, TE2]], R]) -> Flow[Iterable[Dict[R, List[Tuple[TE1, TE2]]]]]: ...

    @overload
    def group_by(self, by: Callable[[TE1, TE2, TE3], R]) -> Flow[Iterable[Dict[R, List[Tuple[TE1, TE2, TE3]]]]]: ...

    @overload
    def group_by(self, by: Callable[[Tuple[TE1, TE2, TE3]], R]) -> Flow[
        Iterable[Dict[R, List[Tuple[TE1, TE2, TE3]]]]]: ...

    @overload
    def group_by(self, by: Callable[[TE1, TE2, TE3, TE4], R]) -> Flow[
        Iterable[Dict[R, List[Tuple[TE1, TE2, TE3, TE4]]]]]: ...

    @overload
    def group_by(self, by: Callable[[Tuple[TE1, TE2, TE3, TE4]], R]) -> Flow[
        Iterable[Dict[R, List[Tuple[TE1, TE2, TE3, TE4]]]]]: ...

    @overload
    def take(self, n: int) -> Flow[T]: ...

    @overload
    def take_if(self, f: Callable[[TE], bool]) -> Flow[T]: ...

    @overload
    def take_if(self, f: Callable[[TE1, TE2], bool]) -> Flow[T]: ...

    @overload
    def take_if(self, f: Callable[[Tuple[TE1, TE2]], bool]) -> Flow[T]: ...

    @overload
    def take_if(self, f: Callable[[TE1, TE2, TE3], bool]) -> Flow[T]: ...

    @overload
    def take_if(self, f: Callable[[Tuple[TE1, TE2, TE3]], bool]) -> Flow[T]: ...

    @overload
    def take_if(self, f: Callable[[TE1, TE2, TE3, TE4], bool]) -> Flow[T]: ...

    @overload
    def take_if(self, f: Callable[[Tuple[TE1, TE2, TE3, TE4]], bool]) -> Flow[T]: ...

    @overload
    def first(self) -> Flow[TE]: ...

    @overload
    def first(self) -> Flow[Tuple[TK, TV]]: ...

    @overload
    def drop(self, n: int) -> Flow[T]: ...

    @overload
    def drop(self, n: int) -> Flow[Tuple[TK, TV]]: ...

    @overload
    def skip(self, n: int) -> Flow[T]: ...

    @overload
    def skip(self, n: int) -> Flow[Tuple[TK, TV]]: ...

    @overload
    def shift(self, n) -> Flow[T]: ...

    @overload
    def concat(self, seq: Iterable[TE]) -> Flow[Iterable[TE]]: ...

    @overload
    def concat(self, seq: Flow[T]) -> Flow[T]: ...

    @overload
    def concat(self, seq1: Iterable[TE], seq2: Iterable[TE]) -> Flow[T]: ...

    @overload
    def concat(self, seq1: Flow[T], seq2: Flow[T]) -> Flow[T]: ...

    @overload
    def concat(self, seq1: Iterable[TE], seq2: Flow[T]) -> Flow[T]: ...

    @overload
    def concat(self, seq1: Flow[T], seq2: Iterable[TE]) -> Flow[T]: ...

    @overload
    def concat(self, seq1: Iterable[TE], seq2: Iterable[TE], seq3: Iterable[TE]) -> Flow[T]: ...

    @overload
    def concat(self, seq1: Iterable[TE], seq2: Iterable[TE], seq3: Iterable[TE], seq4: Iterable[TE]) -> Flow[T]: ...

    @overload
    def concat(self, *seq: Iterable[TE]) -> Flow[T]: ...

    @overload
    def to_list(self) -> Flow[List[TE]]: ...

    @overload
    def to_dict(self) -> Flow[Dict[TE1, TE2]]: ...

    @overload
    def to_dict(self) -> Flow[Dict[TK, TV]]: ...

    @overload
    def to_list(self) -> Flow[List[TE]]: ...

    @overload
    def to_tuple(self) -> Flow[Tuple[TE, ...]]: ...

    @overload
    def to_tuple(self) -> Flow[Tuple[Tuple[TK, TV], ...]]: ...

    @overload
    def to_set(self) -> Flow[Set[TE]]: ...

    @overload
    def to_set(self) -> Flow[Set[Tuple[TK, TV]]]: ...

    @overload
    def all(self) -> Flow[bool]: ...

    @overload
    def all(self, f: Callable[[TE], R]) -> Flow[bool]: ...

    @overload
    def all(self, f: Callable[[TE1, TE2], R]) -> Flow[bool]: ...

    @overload
    def all(self, f: Callable[[TE1, TE2, TE3], R]) -> Flow[bool]: ...

    @overload
    def all(self, f: Callable[[TE1, TE2, TE3, TE4], R]) -> Flow[bool]: ...

    @overload
    def all(self, f: Callable[[TK, TV], R]) -> Flow[bool]: ...

    @overload
    def any(self) -> Flow[bool]: ...

    @overload
    def any(self, f: Callable[[TE], R]) -> Flow[bool]: ...

    @overload
    def any(self, f: Callable[[TE1, TE2], R]) -> Flow[bool]: ...

    @overload
    def any(self, f: Callable[[TE1, TE2, TE3], R]) -> Flow[bool]: ...

    @overload
    def any(self, f: Callable[[TE1, TE2, TE3, TE4], R]) -> Flow[bool]: ...

    @overload
    def any(self, f: Callable[[TK, TV], R]) -> Flow[bool]: ...

    @overload
    def arg_sorted(self) -> Flow[Iterable[int]]: ...

    @overload
    def arg_sorted(self, f: Callable[[TE], R]) -> Flow[Iterable[int]]: ...

    @overload
    def arg_sorted(self, f: Callable[[TE1, TE2], R]) -> Flow[Iterable[int]]: ...

    @overload
    def arg_sorted(self, f: Callable[[TE1, TE2, TE3], R]) -> Flow[Iterable[int]]: ...

    @overload
    def arg_sorted(self, f: Callable[[TE1, TE2, TE3, TE4], R]) -> Flow[Iterable[int]]: ...

    @overload
    def intersects(self, *others: Iterable[TE]) -> Flow[Set[TE]]: ...

    @overload
    def intersects(self, *others: Iterable[Tuple[TK, TV]]) -> Flow[Set[Tuple[TK, TV]]]: ...

    @overload
    def union(self, *others: Iterable[TE]) -> Flow[Set[TE]]: ...

    @overload
    def union(self, *others: Iterable[Tuple[TK, TV]]) -> Flow[Set[Tuple[TK, TV]]]: ...


x: Flow[int]

