from dataclasses import dataclass

@dataclass
class Task():
        id: int
        title: str
        descitpion: str

        
        @classmethod
        def from_dict(cls, data: dict) -> 'Task':
                return cls(
                        id = data.get('id'),
                        title = data.get('title'),
                        description = data.get('description')
                        )