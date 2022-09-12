from bot import EcoBot


class RunApp():
    def __init__(self, link):
        bot_count = 2
        headless_checkbox = True
        bot_multiplier_checkbox = True
        black_video_checkbox = True
        bot = EcoBot(link, bot_count, headless_checkbox, bot_multiplier_checkbox, black_video_checkbox)
        bot.run_chrome()

        


if __name__ == '__main__':
    start = RunApp("https://loco.gg/stream/a1e91e80-2261-49f3-bf92-de37145d3233")
    