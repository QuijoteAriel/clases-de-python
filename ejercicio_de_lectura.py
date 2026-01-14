import time
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Optional, Any

class ProcessorBase(ABC):
    @abstractmethod
    def execute(self, payload: Any) -> Any:
        pass

def logger_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[LOG] {func.__name__.upper()} completado en {duration:.4f}s")
        return result
    return wrapper

class Node:
    def __init__(self, data: Dict[str, Any]):
        self.id = uuid.uuid4().hex[:8]
        self.timestamp = datetime.now()
        self.content = data.get("content", "")
        self.weight = data.get("importance", 1)
        self.status = "pending"

    def __repr__(self):
        return f"<Node {self.id} | W:{self.weight} | {self.status}>"

class Engine(ProcessorBase):
    def __init__(self, threshold: int = 5):
        self.threshold = threshold
        self.history: List[Node] = []
        self._buffer: List[Node] = []

    def ingest(self, raw_data: List[Dict]):
        for item in raw_data:
            new_node = Node(item)
            self._buffer.append(new_node)
        self._sort_buffer()

    def _sort_buffer(self):
        # El criterio de ordenación es clave aquí
        self._buffer.sort(key=lambda x: x.weight, reverse=True)

    @logger_wrapper
    def execute(self, limit: Optional[int] = None) -> List[Node]:
        processed = []
        to_process = self._buffer[:limit] if limit else self._buffer
        
        for node in to_process:
            try:
                if node.weight >= self.threshold:
                    node.status = "processed"
                else:
                    node.status = "deferred"
                
                processed.append(node)
                self.history.append(node)
            except Exception as e:
                node.status = "error"
                print(f"Error en nodo {node.id}: {e}")

        # Limpiar buffer de lo procesado
        self._buffer = [n for n in self._buffer if n not in processed]
        return processed

    def get_report(self):
        stats = {
            "total": len(self.history),
            "processed": len([n for n in self.history if n.status == "processed"]),
            "deferred": len([n for n in self.history if n.status == "deferred"])
        }
        return stats

# --- Bloque de ejecución ---
if __name__ == "__main__":
    # Simulación de entrada de datos
    data_stream = [
        {"content": "Update system kernels", "importance": 9},
        {"content": "Clear temp files", "importance": 2},
        {"content": "Rebuild database indexes", "importance": 7},
        {"content": "Minor UI adjustment", "importance": 3},
        {"content": "Security patch v2", "importance": 10}
    ]

    core = Engine(threshold=6)
    
    print("--- Iniciando Ingesta ---")
    core.ingest(data_stream)
    
    print("\n--- Estado del Buffer ---")
    for n in core._buffer:
        print(n)

    print("\n--- Ejecutando Ciclo ---")
    batch = core.execute(limit=3)
    
    print("\n--- Resultados del Batch ---")
    for n in batch:
        print(f"ID: {n.id} -> Status: {n.status} ({n.content})")

    print("\n--- Informe Final ---")
    print(core.get_report())
