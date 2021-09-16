import yaml


class Dialogue:
    """ Attach to any game object we want to have a dialogue system for. """

    def __init__(self):
        self.branches = []
        self.active = True  # Whether the dialogue is shown and interactable

    # Add a branch to this dialogue
    def add_branch(self, branch):
        self.branches.append(branch)

    # Get a branch belonging to this dialogue with the given id
    def get_branch(self, id):
        for branch in self.branches:
            if branch.id == id:
                return branch
        return None

    def load_tree(self, name):
        # name provided by the attached game object
        with open("Assets/Dialogues/" + name + ".yml", "r") as f:
            data = yaml.safe_load(f.read())
            self.active = data["active"]

            for branch_data in data["branches"]:
                branch = Branch(branch_data["id"], branch_data["content"])

                for link in branch_data["links"]:
                    branch.add_link(link["content"], link["dialogue"])

                self.branches.append(branch)


class Branch:
    def __init__(self, id, content) -> None:
        self.id = id  # Unique string to lookup
        self.content = content  # What the user reads
        self.links = []  # The possible links to other branches from this branch
        self.active = True  # Whether the branch is shown and interactable

    def add_link(self, text, dialogue_id):
        # [0] text | [1] dialogue id
        self.links.append((text, dialogue_id))

    def print_to_console(self):
        print("id: " + self.id + "\nContent: " + self.content)
        link_output = ""

        for link in self.links:
            link_output += link.content + " [" + link.dialogue + "]\n"
        print("Links:\n" + link_output)
