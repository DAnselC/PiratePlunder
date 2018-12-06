"""
Game Lobby class to keep information about each player in a game

Written by Trevor Zapiecki
"""

from .player import Player
from . import events
from .task_generator import TaskGenerator

class GameLobby:
    def __init__(self, lobby_id, numPlayers):
        """Constructor for Lobby"""

        self.lobby_id = lobby_id
        self.numPlayers = numPlayers
        self.connectedPlayers = 0
        self.players = {}       # KEY: user_id/cookies, VALUE: Player object

        # KEY: user/id cookie, VALUE: first task that user has to complete
        self.initial_task_assignments = {}

        # KEY: userid/cookie, VALUE: a list of tasks that this particular 
        # user can complete (should appear with buttons on their screen)
        self.user_tasks = {}

    def add_player(self, player):
        self.players[player.user_id] = player

    

    def assign_tasks(self):
        """
        Assign tasks to each player, both the task that they must complete
        as well as the list of tasks that they are able to complete 
        (which buttons should appear on their screen)
        """

        self.task_generator = TaskGenerator(len(self.players))

        player_cookies = list(self.players.keys())
        initial_task_ids = list(self.task_generator.current_tasks.keys())
        usable_task_ids = list(self.task_generator.usable_tasks.keys())

        # Assign tasks to be completed. Tasks are assigned in no particular order, 
        # just however the dictionaries organize their keys.
        for i in range(len(player_cookies)):

            player_cookie = player_cookies[i]
            task_id = initial_task_ids[i]

            # Assign task to do
            self.initial_task_assignments[player_cookie] = self.task_generator.current_tasks[task_id]


            # Assign a list of tasks that each user can complete on their own

            index_of_first_task = i * TaskGenerator.NUM_TASKS_PER_PLAYER

            # initialize with empty list, so we can add tasks to it in loop
            self.user_tasks[player_cookie] = []
            for j in range(TaskGenerator.NUM_TASKS_PER_PLAYER):

                # figure out which task we can add from usable_tasks
                interactable_task_id = usable_task_ids[ (i * TaskGenerator.NUM_TASKS_PER_PLAYER) + j ]

                # add that task
                self.user_tasks[player_cookie].append(self.task_generator.usable_tasks[interactable_task_id])
        









