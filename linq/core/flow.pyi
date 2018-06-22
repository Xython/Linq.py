from typing import Generic, TypeVar, Iterable, Callable, overload, List, Tuple, Set, Dict, Any, Union, Mapping, \
    Sequence, Optional
from .collections import ScanGenerator

TE = TypeVar('TE')
TE1 = TypeVar('TE1')
TE2 = TypeVar('TE2')
TE3 = TypeVar('TE3')
TE4 = TypeVar('TE4')

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
T = TypeVar('T', Iterable[TE], Mapping[TK, TV], Iterable[Tuple[TE1, TE2]], Iterable[Tuple[TE1, TE2, TE3, TE4]])

extension_std: function
extension_std_no_box: function
extension_class: function
unbox_if_flow: function


class Flow(Generic[T]):
    _: T

    @overload
    def __new__(cls, value: Mapping[TK, TV]) -> Flow[Mapping[TK, TV]]: ...

    @overload
    def __new__(cls, value: Iterable[TE]) -> Flow[Iterable[TE]]: ...

    @overload
    def sum(self: Flow[Iterable[int]]) -> int: ...

    @overload
    def sum(self: Flow[Iterable[int]], f: Callable[[int], U]) -> U: ...

    @overload
    def sum(self: Flow[Iterable[float]]) -> float: ...

    @overload
    def sum(self: Flow[Iterable[float]], f: Callable[[float], U]) -> U: ...

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
    def then(self, f: Callable[[Mapping[TK, TV]], R]) -> R: ...

    @overload
    def then(self, f: Callable[Iterable[TE], R]) -> R: ...

    @overload
    def scan(self, f: Callable[[R, TE], R], start_elem: R) -> Flow[Iterable[R]]: ...

    @overload
    def reduce(self, f: Callable[[R, TE], R], start_elem: Optional[R] = None) -> R: ...

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
    def filter(self, f: Callable[[TK, TV], bool]) -> Iterable[Tuple[TK, TV]]: ...

    @overload
    def filter(self, f: Callable[[Tuple[TK, TV]], bool]) -> Iterable[Tuple[TK, TV]]: ...

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
    def aggregate(self, fn1: Callable[[T], V1], fn2: Callable[[T], V2]) -> Tuple[V1, V2]: ...

    @overload
    def aggregate(self, fn1: Callable[[T], V1], fn2: Callable[[T], V2], fn3: Callable[[T], V3]) -> Tuple[
        V1, V2, V3]: ...

    @overload
    def aggregate(self, fn1: Callable[[T], V1], fn2: Callable[[T], V2], fn3: Callable[[T], V3],
                  fn4: Callable[[T], V4]) -> Tuple[V1, V2, V3, V4]: ...

    @overload
    def aggregate(self, *functions: Callable[[T], R]) -> Tuple[R, ...]: ...

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
    def first(self) -> TE: ...

    @overload
    def first(self) -> Tuple[TK, TV]: ...

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
    def to_list(self) -> List[TE]: ...

    @overload
    def to_dict(self) -> Dict[TE1, TE2]: ...

    @overload
    def to_dict(self) -> Dict[TK, TV]: ...

    @overload
    def to_list(self) -> List[TE]: ...

    @overload
    def to_tuple(self) -> Tuple[TE, ...]: ...

    @overload
    def to_tuple(self) -> Tuple[Tuple[TK, TV], ...]: ...

    @overload
    def to_set(self) -> Set[TE]: ...

    @overload
    def to_set(self) -> Set[Tuple[TK, TV]]: ...

    @overload
    def all(self) -> bool: ...

    @overload
    def all(self, f: Callable[[TE], R]) -> bool: ...

    @overload
    def all(self, f: Callable[[TE1, TE2], R]) -> bool: ...

    @overload
    def all(self, f: Callable[[TE1, TE2, TE3], R]) -> bool: ...

    @overload
    def all(self, f: Callable[[TE1, TE2, TE3, TE4], R]) -> bool: ...

    @overload
    def all(self, f: Callable[[TK, TV], R]) -> bool: ...

    @overload
    def any(self) -> bool: ...

    @overload
    def any(self, f: Callable[[TE], R]) -> bool: ...

    @overload
    def any(self, f: Callable[[TE1, TE2], R]) -> bool: ...

    @overload
    def any(self, f: Callable[[TE1, TE2, TE3], R]) -> bool: ...

    @overload
    def any(self, f: Callable[[TE1, TE2, TE3, TE4], R]) -> bool: ...

    @overload
    def any(self, f: Callable[[TK, TV], R]) -> bool: ...

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
