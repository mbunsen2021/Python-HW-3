# Question 6
# Madison Bunsen
# Z23631556

import unittest

class Entry:
    """Base class for an item with a parent and child"""

    def __init__(self, name: str, parent: "Entry | None" = None) -> None:
        self.name = name
        self._parent = parent

    def parent(self) -> "Entry | None":     
        """If the entry has a parent then return it"""
        return self._parent

    def size(self) -> int:
        """Return this entry's size in bytes"""
        raise NotImplementedError("Entry subclasses must implement size()")

    def absolute_path(self) ->list["Entry"]:
        if self.parent() is not None:
            return [self] + self.parent().absolute_path()
        
        return [self]


 

class File(Entry):
    def __init__(self, name: str, bytes_used: int, parent: Entry | None = None) -> None:
        super().__init__(name, parent)

        if isinstance(bytes_used, bool) or not isinstance(bytes_used, int):
            raise TypeError("bytes must be an integer")
        if bytes_used < 0:
            raise ValueError("bytes must be a nonnegative")
        self.bytes_used = bytes_used

    def size(self) -> int:
        return self.bytes_used




class Folder(Entry):
    def __init__(self, name: str, parent: Entry | None = None) -> None:
        super().__init__(name,parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        entry._parent = self
        self._children.append(entry) 

    def children(self) -> tuple[Entry, ...]:
        return tuple(self._children)


    def size(self) -> int:
        return sum(entry.size() for entry in self._children)

def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    if isinstance(minimum_size, bool) or not isinstance(minimum_size, int):
        raise TypeError("minimum_size must be a nonnegative")
    if minimum_size < 0:
        raise ValueError("minimum_size must be a nonnegative")

    if isinstance(entry, File):
        return [entry] if entry.size() >= minimum_size else []    

    if isinstance(entry, Folder):
        found: list[File] = []
        for child in entry.children():
            found.extend(find_large_files(child, minimum_size))
        return found

    return []


class EntryTests(unittest.TestCase):
    print( "Madison Bunsen | Z23631556")
    def setUp(self) -> None:
        self.root = Folder("root")
        self.documents = Folder("documents")
        self.projects = Folder("projects")

        self.root.add(self.documents)
        self.documents.add(self.projects)

        self.small_file = File("notes.txt", 100)
        self.large_file = File("report.pdf", 1_000)
        self.largest_file = File("archive.zip", 5_000)

        self.root.add(self.small_file)
        self.documents.add(self.large_file)
        self.projects.add(self.largest_file)

    def test_absolute_path(self) -> None:
        self.assertEqual(
            self.largest_file.absolute_path(),
            [self.largest_file, self.projects, self.documents, self.root],
        )
        self.assertEqual(self.root.absolute_path(), [self.root])

    def test_outer_folder_size(self) -> None:
        self.assertEqual(self.root.size(), 6_100)

    def test_find_large_files_at_two_thresholds(self) -> None:
        self.assertEqual(
            find_large_files(self.root, 1_000),
            [self.largest_file, self.large_file],
        )
        self.assertEqual(
            find_large_files(self.root, 5_000),
            [self.largest_file],
        )



if __name__ == "__main__":
    unittest.main()











    



        
        

        










