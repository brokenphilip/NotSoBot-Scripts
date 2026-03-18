# NotSoBot Scripts
This repository contains an assortment of (relatively) small and useful Python scripts that I've made, designed to be embedded and used within NotSoBot's tag system (although, these scripts can easily be adjusted to work just about anywhere else).

# Usage
### Requirements
[NotSoBot](https://notsobot.com/) must be added to your server, with at least the ability to read and send messages.

> [!NOTE]
> The following installation and updating guides assume that:
> 1. the bot will respond to commands when mentioned/pinged,
> 2. the tag is named "run", and
> 3. you have the ability to add commands and edit this tag
>
> If this is not the case, update the following commands accordingly.

> [!IMPORTANT]
> As of 2020-2021, **NotSoBot tags are no longer global**. If you want access to the tag in multiple servers, you will have to perform these steps for each server NotSoBot is in.

### Installation
Simply add a new dummy tag called "run" by entering the following command:
```
@NotSoBot#9555 tag add run blablabla
```
After adding the tag, update it by following the steps below.

### Checking for updates
The current version of the **NotSoBot Python Script Runner** command is: v1.0

To see which version you have, check the first line when running the command:
```
@NotSoBot#9555 tag raw run
```

### Updating
Edit your "run" tag by copying and running the command in [COMMAND.txt](https://raw.githubusercontent.com/brokenphilip/NotSoBot-Scripts/refs/heads/main/COMMAND.txt).

# Scripts
Arguments in `<>` are mandatory, while arguments in `[]` are optional.

Optional arguments ending with `...` imply you can pass an indefinite amount of arguments.

> [!NOTE]
> The following example usage commands assume that:
> 1. the bot will respond to commands prefixed with `.` and
> 2. the main tag is named "run"
>
> If this is not the case, update the following commands accordingly.

### 📌 Help v1.0
**Usage** `.t run help`

Shows a list of all available commands.

### 📌 Info v1.0
**Usage:** `.t run info [any...]`

Returns all the information currently accessible through the main tag:
- the username, discrim, id, nickname and avatar URL of the person who ran the command,
- the name, id and member count of the server where the command was run,
- the name and id of the channel where the command was run,
- `[any...]` arguments, including the command name "info", as well as the number of arguments,
- the bot prefix, and
- a randomly selected
  - user,
  - online user, and
  - channel

### TF2 Next Full Moon v1.0
**Usage:** `.t run fm [count]`

Gets the dates and times for the next `count` Full Moon holidays in Team Fortress 2. If `count` is not entered, only one result is returned.

### PvZ: GW22 Next Quest Reset v1.0
**Usage:** `.t run gw2 [count]`

Gets the dates and times for the next `count` cycles/resets of (star) quests in Plants vs Zombies: Garden Warfare 2. If `count` is not entered, only one result is returned.

### Progress Bar v1.0
**Usage:** `.t run progressbar`

Shows the current year progress bar percentage.

### PvZ: GW22 Next Town Hall Event v1.0
**Usage:** `.t run th [count]`

Gets the names, dates and times for the next `count` Town Hall events in Plants vs Zombies: Garden Warfare 2. If `count` is not entered, only one result is returned.
