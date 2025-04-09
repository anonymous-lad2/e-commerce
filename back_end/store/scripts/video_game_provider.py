import random


class VideoGameProvider:
    def __init__(self, faker):
        self.faker = faker
        self.genres = ['Action', 'Adventure', 'RPG', 'Shooter', 'Puzzle',
                        'Platformer', 'Strategy', 'Simulation', 'Sports',
                          'Horror', 'Sci-Fi', 'Fighting']
        self.prefixes = [
            'The', 'Kingdom of', 'Quest for', 'Darkness of', 'Warrior\'s',
              'Rise of', 'Tales of', 'Chronicles of', 'Legends of',
                'Empire of', 'Rise and Fall of', 'City of', 'Adventures of',
                  'Beyond the', 'Age of'
        ]
        self.adjectives = [
            'Epic', 'Mystic', 'Lost', 'Uncharted', 'Forsaken', 'Forbidden',
              'Legendary', 'Ancient', 'Cursed', 'Dark', 'Eternal',
                'Frostbitten', 'Fallen', 'Unseen', 'Endless', 'Shadowed',
                  'Haunted', 'Forgotten', 'Brave'
        ]
        self.nouns = [
            'World', 'Realm', 'Saga', 'Warrior', 'Champion', 'Shadow', 'Hero',
              'Battlefield', 'Kingdom', 'Odyssey', 'Empire', 'Horizon',
                'Frontier', 'Knight', 'Legacy', 'War', 'Beast', 'Fury',
                  'Victory', 'Purge'
        ]
        self.descriptions = [
            "An immersive experience where you embark on a journey through"
            " mystical lands, battling creatures and solving puzzles.",
            "An action-packed adventure that will test your reflexes and"
            " strategic thinking.",
            "A role-playing game where you take on the role of a hero, complete"
            " quests, and defeat powerful enemies.",
            "Explore an open world filled with hidden secrets and challenging"
            " enemies.",
            "A tactical simulation where you build, manage, and conquer the"
            " battlefield with your troops.",
            "A fast-paced game that combines combat and strategy to create"
            " thrilling multiplayer experiences.",
            "Embark on a heroic quest to save the world from a dark, ancient"
            " power.",
            "Battle through dangerous terrain, fight fierce creatures, and"
            " uncover hidden artifacts in a fantasy setting.",
            "Survive in a post-apocalyptic world filled with danger and"
            " challenges.",
            "Fight your way through intense arenas and rise to become the"
            " champion of the world.",
            "Solve challenging puzzles and uncover the secrets of a forgotten"
            " civilization.",
            "In a world of endless possibilities, you must fight to survive and"
            " build your legacy.",
            "Embark on a space-faring journey to explore distant galaxies and"
            " battle alien enemies.",
            "Defend your kingdom from invading forces and build a new empire"
            " from the ground up.",
            "Uncover dark secrets and explore an ancient world shrouded in"
            " mystery and danger."
        ]


    def video_game_title(self):
        title = f"{random.choice(self.prefixes)} {random.choice(self.adjectives)} {random.choice(self.nouns)}"
        return title
    
    def video_game_category(self):
        return random.choice(self.genres)
    
    def video_game_description(self):
        return random.choice(self.descriptions)
    