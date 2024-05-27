from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a Pydantic model for a task
class Task(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

# In-memory storage for tasks
tasks = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            removed_task = tasks.pop(index)
            return removed_task
    raise HTTPException(status_code=404, detail="Task not found")

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
