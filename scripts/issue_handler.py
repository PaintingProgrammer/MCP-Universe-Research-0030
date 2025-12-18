import sys
import os

def handle_issue(payload):
    action = payload.get('action')
    issue = payload.get('issue', {})
    labels = [label['name'] for label in issue.get('labels', [])]
    
    if action == 'opened':
        print(f"Issue opened: {issue.get('title')}")
        print(f"Labels: {labels}")
        
        if 'bug' in labels:
            print("Comment: Thank you. We will fix it.")
        elif 'feature' in labels:
            print("Comment: Thank you, we will consider to include this feature.")
        elif 'discussion' in labels:
            print("Comment: Thanks for starting this discussion! We welcome community input.")

if __name__ == "__main__":
    # In a real workflow, this would read from stdin or an environment variable
    # For testing purposes, we simulate it
    pass
