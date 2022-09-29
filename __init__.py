

class Node:
  def __init__(self, data: float) -> None:
    self.data = data
    self.right = None
    self.left = None

  def print(self) -> None:
    if self.left:
      self.left.print()

    print(self.data)

    if self.right:
      self.right.print()

  def insert(self, data: float) -> None:
    if self.data is None:
      self.data = data
      return

    if data < self.data:
      if self.left is None:
        self.left = Node(data)

      else:
        self.left.insert(data)

    else:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.insert(data)


def main() -> None:
  root = Node(0)
  root.insert(10)
  root.insert(-10)
  root.insert(180)
  root.insert(-180)

  root.print()

if __name__ == "__main__":
  main()