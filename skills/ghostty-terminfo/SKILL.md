---
name: ghostty-terminfo
description: >
  Fixes "unknown terminal" errors when SSHing from Ghostty (or other modern terminals like Kitty, WezTerm) into a Linux server that doesn't recognize the terminal type. Trigger this skill whenever the user sees errors like `tput: unknown terminal "xterm-ghostty"`, `Error opening terminal`, or any complaint about an unknown or unrecognized TERM variable on a remote Linux machine. Also trigger when the user asks how to get ncurses, terminal UI programs, or color output working over SSH from Ghostty.
---

# Ghostty Terminfo Fix

## The Problem

When SSHing from Ghostty into a Linux server, you may see:

```
tput: unknown terminal "xterm-ghostty"
Error opening terminal: xterm-ghostty
```

This happens because Ghostty sets `TERM=xterm-ghostty`, but the remote machine doesn't have Ghostty's terminfo entry installed — so it has no idea how to handle colors, cursor movement, or terminal UI features. The Mac knows what Ghostty is; the server doesn't.

The same issue occurs with other modern terminals (Kitty sets `TERM=xterm-kitty`, WezTerm uses `wezterm`, etc.).

## Quick Fix (Get Unstuck Now)

On your Mac, connect with a known-good terminal type:

```bash
TERM=xterm-256color ssh user@server
```

Or if you're already logged in:

```bash
export TERM=xterm-256color
```

This makes the server treat your terminal like a standard 256-color xterm. Fast, always works.

## Proper Fix (Install the Terminfo Entry)

This teaches the server what your terminal actually is, so you don't have to work around it every time.

### Step 1 — Export the terminfo entry from your Mac

```bash
infocmp xterm-ghostty > /tmp/xterm-ghostty.terminfo
```

For other terminals, replace `xterm-ghostty` with your `$TERM` value (e.g., `xterm-kitty`).

### Step 2 — Copy it to the server

```bash
scp /tmp/xterm-ghostty.terminfo user@server:/tmp/
```

### Step 3 — Install it on the server

```bash
ssh user@server
tic -x /tmp/xterm-ghostty.terminfo
```

This installs the entry into `~/.terminfo/` for your user. No root needed.

### Step 4 — Reconnect and verify

```bash
exit
ssh user@server
echo $TERM       # should show: xterm-ghostty
tput colors      # should show: 256
```

If `tput colors` returns 256, you're done.

## Optional: Lock It In via SSH Config

If you want `xterm-256color` permanently for a specific host (simpler, no terminfo needed):

Edit `~/.ssh/config` on your Mac:

```sshconfig
Host my-server
  HostName 192.168.x.x
  User youruser
  SetEnv TERM=xterm-256color
```

This is boring but reliable for servers you don't want to bother installing terminfo on.

## Mental Model

`TERM` is just a label. `terminfo` is the instruction manual for that label.

Ghostty says "I'm `xterm-ghostty`." The remote server needs the matching instruction manual so programs know how to handle colors, cursor movement, backspace, function keys, and terminal UI rendering. No drama — just teach the server what Ghostty is.

## Which Fix to Use?

- **Just want things working right now?** → `export TERM=xterm-256color`
- **Using this server regularly?** → Install the terminfo entry (`infocmp` + `scp` + `tic`)
- **Don't care about native Ghostty features on this server?** → Use the SSH config `SetEnv` approach

## Distro Notes

- **Arch Linux**: `tic` is part of `ncurses`, installed by default.
- **Debian/Ubuntu**: same — `tic` is available without extra packages.
- **Minimal containers**: may need `ncurses-bin` (`apt install ncurses-bin`) before `tic` works.
