os: mac
-

# run the lila app in a "lila" tmux session:
# tmux new-session -d -s lila -c ~/projects/lila
# tmux send-keys -t lila 'devenv shell' Enter
# TODO: run the above on startup
lila restart:
    user.system_command_nb("/opt/homebrew/bin/tmux send-keys -t lila -X cancel || true; /opt/homebrew/bin/tmux send-keys -t lila C-c 'sbt run' Enter")
    app.notify("Restarting Lila")
key(f4):
    user.system_command_nb("/opt/homebrew/bin/tmux send-keys -t lila -X cancel || true; /opt/homebrew/bin/tmux send-keys -t lila C-c 'sbt run' Enter")
    app.notify("Restarting Lila")

lila stop:
    user.system_command_nb("/opt/homebrew/bin/tmux send-keys -t lila -X cancel || true; /opt/homebrew/bin/tmux send-keys -t lila C-c 'sbt stop' Enter")
    app.notify("Stopping Lila")

lila format: "sbt scalafmtAll\n"
