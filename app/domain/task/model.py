from dataclasses import dataclass

@dataclass
class Task():
        id: int
        titulo: str
        descricao: str
        user_id: int

        @classmethod
        def from_dict(cls, data: dict) -> 'Task':
                return cls(
                        id = data.get('id'),
                        titulo = data.get('titulo'),
                        descricao = data.get('descricao'),
                        user_id = data.get('user_id')
                        )