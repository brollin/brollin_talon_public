os: mac
-

# run the lila app in the "lila" tmux session
key(f4): user.system_command("/opt/homebrew/bin/tmux send-keys -t lila C-c '' 'bloop run lila -m lila.app.Lila -c ~/projects/lila/.bloop' Enter")
