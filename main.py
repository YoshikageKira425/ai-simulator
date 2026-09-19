import arcade
from src.views.game_view import GameView
import argparse
from src.constant import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    parser = argparse.ArgumentParser(description="2D Racing AI Simulation Controller")

    parser.add_argument("--game", action="store_true", help="Launch manual player mode")
    args = parser.parse_args()

    if args.game or not args.game:
        play_game()


def play_game():
    print("Playing game")

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.show_view(GameView())
    arcade.run()


if __name__ == "__main__":
    main()
