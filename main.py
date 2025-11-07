import os
from dotenv import load_dotenv


load_dotenv()

import yaml
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
 


# Step 1: Define a tool mapper
# This maps YAML tool names to actual tool instances.
# Add more here if you introduce new tools.
TOOL_MAP = {
    'SerperDevTool': SerperDevTool()
}

# Step 2: Load YAML files
# Assume files are in 'config/' folder.
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

agents_data = load_yaml('config/agents.yaml')['agents']
tasks_data = load_yaml('config/tasks.yaml')['tasks']

# Step 3: Create Agents from YAML
agents = {}
for agent_data in agents_data:
    # Extract tool instances if specified
    tools = []
    if 'tools' in agent_data:
        for tool_name in agent_data['tools']:
            if tool_name in TOOL_MAP:
                tools.append(TOOL_MAP[tool_name])
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
    
    # Create the Agent object
    agent = Agent(
        role=agent_data['role'],
        goal=agent_data['goal'],
        backstory=agent_data['backstory'],
        verbose=agent_data.get('verbose', False),
        tools=tools
    )
    # Map by name for task assignment
    agents[agent_data['name']] = agent

# Step 4: Create Tasks from YAML
tasks = []
for task_data in tasks_data:
    # Get the agent object by name
    agent_name = task_data['agent']
    if agent_name not in agents:
        raise ValueError(f"Unknown agent: {agent_name}")
    
    # Create the Task object
    task = Task(
        description=task_data['description'],
        expected_output=task_data['expected_output'],
        agent=agents[agent_name]
    )
    tasks.append(task)

# Step 5: Assemble the Crew
crew = Crew(
    agents=list(agents.values()),  # All agents
    tasks=tasks,                   # All tasks in sequence
    process=Process.sequential,    # Run tasks one after another
    verbose=True                      # Detailed logging
)

# Step 6: Run the Crew
# Example: Pass the topic as input (can be from CLI or user input)
topic = input("Enter the historical topic:  ")  # Or hardcode for testing, e.g., "The Fall of the Roman Empire"
result = crew.kickoff(inputs={'topic': topic})

# Output the final result (the polished script)
print("Final Script:")
print(result)