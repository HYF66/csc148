import course
import criterion
import grouper
import pytest
from typing import List, Set, FrozenSet


@pytest.fixture
def group(students) -> grouper.Group:
    return grouper.Group(students)


def get_member_ids(grouping: grouper.Grouping) -> Set[FrozenSet[int]]:
    member_ids = set()
    for group in grouping.get_groups():
        ids = []
        for member in group.get_members():
            ids.append(member.id)
        member_ids.add(frozenset(ids))
    return member_ids


def compare_groupings(grouping1: grouper.Grouping,
                      grouping2: grouper.Grouping) -> None:
    assert get_member_ids(grouping1) == get_member_ids(grouping2)

class TestGroup:
    def test___len__(self, group) -> None:
        assert len(group) == 4

    def test___contains__(self, group, students) -> None:
        for student in students:
            assert student in group

    def test___str__(self, group, students) -> None:
        for student in students:
            assert student.name in str(group)

    def test_get_members(self, group) -> None:
        ids = set()
        for member in group.get_members():
            ids.add(member.id)
        assert ids == {1, 2, 3, 4}

class TestGrouping:
    def test___len__(self, greedy_grouping) -> None:
        assert len(greedy_grouping) == 2

    def test___str__(self, greedy_grouping) -> None:
        lines = str(greedy_grouping).splitlines()
        assert len(lines) == 2

        in_lines = []
        for group in greedy_grouping.get_groups():
            in_line = []
            for members in group.get_members():
                name = members.name
                assert name in str(greedy_grouping)
                if name in lines[0]:
                    in_line.append(0)
                    assert name not in lines[1]
                if name in lines[1]:
                    in_line.append(1)
                    assert name not in lines[0]
            assert len(set(in_line)) == 1
            assert in_line[0] not in in_lines
            in_lines.append(in_line[0])

    def test_add_group(self, group) -> None:
        grouping = grouper.Grouping()
        grouping.add_group(group)
        assert group in grouping._groups

    def test_get_groups(self, students) -> None:
        group = grouper.Group(students[:2])
        grouping = grouper.Grouping()
        grouping.add_group(group)
        assert get_member_ids(grouping) == {frozenset([1, 2])}



if __name__ == '__main__':
    pytest.main(['example_tests.py'])
