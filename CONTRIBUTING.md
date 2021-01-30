# Basic Workflow

### Selecting a ticket
- To start you need to assign a ticket to yourself, so navigate to the [issues page](https://github.com/LujainKhalaf/SOEN341/issues), click into an issue and on the right hand side under `assignes` assign yourself from the dropdown menu.
- Now in the [project board](https://github.com/LujainKhalaf/SOEN341/projects/1) drag your card over to the `In Progress` column.

### Updating your local repository
When you want to start on a new ticket first you need to make sure you are up to date with the main branch. In the root of the project
```
git checkout main
git pull
```
### Creating your branch
Next you need to create a new branch for your ticket, the [BRANCH-NAME] will depend on what type of ticket you are doing i.e. a bug, feature, or configuration. See the `Naming Conventions` section below for details on naming branches, commits, and pull requests.
```
git checkout -b [BRANCH-NAME]
```
### Adding your changes
Now that you are on a fresh branch you can start making the code updates. Once you are ready with your updates (this doesn't mean everything is done just that you are at a place that you want to 'save') you will 'add' your changes
```
git add [FILE/PATH]
```
or if you want to add all the files that have been changes
```
git add .
```
### Commiting your changes
Next commit your changes with a descriptive message about what has been done
```
git commit -m "commit message"
```
### Pushing your changes
Then simply push your branch with the changes to the remote repository. If it is your first push on the branch use this command.
```
git push --set-upstream origin [BRANCH-NAME]
```
If it isn't the first push use
```
git push
```
The `[BRANCH-NAME]` will be the name of the branch you are currently working on.

Now your changes are pushed to the remote repository. Next we will create a pull request (pr) for the branch to merge into the `main` branch.
### Creating a pull request
- Navigate in your web browser to the [pull request page](https://github.com/LujainKhalaf/SOEN341/pulls) for the repo and click `New Pull Request`.

- Click the `compare` dropdown and select your branch name (the arrow should point from your branch name to main). Then click the green `Create Pull Request` button.

- Set a title for the pull request defined in the `Naming Conventions` section below and any relevent details in the description. Then click the `Create Pull Request` button again. Your pr is now up for others to review.

- Now make sure to go to the [project board](https://github.com/LujainKhalaf/SOEN341/projects/1) and move your card over to the `In Code Review` column.

# Naming Conventions

The standard naming convention for naming branches, commits, and pull requests is as follows.

### Branches

Branches should be named with the following template `[ticket-type]/[issue-number]_short_description`

An example of this is for creating a branch to update the readme file `doc/10_add_readme_info`

For a list of `ticket-types` see the `ticket-types` section below.

The `issue-number` is the number associated with the ticket / issue on the [issues page](https://github.com/LujainKhalaf/SOEN341/issues)

### Pull Requests

This is refering to the pull request title which should describe in short what the PR is doing as well as including the issue id. An example is `#22 new api endpoint for likes`

### Commits

Commits have no defined naming template, but they should be descriptive of what changes were made in that commit and start with the id of the issue it is associated to i.e. #10 an example is `#10 added my name to the readme file`

### Ticket Types

- feat
- bug
- doc
- config
- refactor