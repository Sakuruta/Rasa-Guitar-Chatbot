from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBeriInfoKunci(Action):

    def name(self) -> Text:
        return "action_beri_info_kunci"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        kunci = tracker.get_slot("nama_kunci")

        database_kunci = {
            "c": (
                "    C\n"
                "    X   O   O   O   O   O\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   | 1 |   |  <- Fret 1\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   | 2 |   |   |   |  <- Fret 2\n"
                "  +---+---+---+---+---+---+\n"
                "  |   | 3 |   |   |   |   |  <- Fret 3\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 4\n"
                "  +---+---+---+---+---+---+\n"
                "    E   A   D   G   B   e"
            ),
            "g": (
                "    G\n"
                "    O   O   O   O   O   O\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 1\n"
                "  +---+---+---+---+---+---+\n"
                "  |   | 1 |   |   |   |   |  <- Fret 2\n"
                "  +---+---+---+---+---+---+\n"
                "  | 2 |   |   |   | 3 | 4 |  <- Fret 3\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 4\n"
                "  +---+---+---+---+---+---+\n"
                "    E   A   D   G   B   e"
            ),
            "am": (
                "    Am\n"
                "    X   O   O   O   O   O\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   | 1 |   |  <- Fret 1\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   | 2 | 3 |   |   |  <- Fret 2\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 3\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 4\n"
                "  +---+---+---+---+---+---+\n"
                "    E   A   D   G   B   e"
            ),
            "d": (
                "    D\n"
                "    X   X   O   O   O   O\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 1\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   | 1 |   | 2 |  <- Fret 2\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   | 3 |   |  <- Fret 3\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 4\n"
                "  +---+---+---+---+---+---+\n"
                "    E   A   D   G   B   e"
            ),
            "bm": (
                "    Bm\n"
                "    X   O   O   O   O   X\n"
                "  +---+---+---+---+---+---+\n"
                "  | 1 | 1 | 1 | 1 | 1 | 1 |  <- Fret 2 (Barre)\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 3\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   | 3 | 4 |   |   |  <- Fret 4\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 5\n"
                "  +---+---+---+---+---+---+\n"
                "    E   A   D   G   B   e"
            ),
            "dm": (
                "    Dm\n"
                "    X   X   O   O   O   O\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   | 1 |  <- Fret 1 (Jari 1 di senar e)\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   | 2 |   |   |  <- Fret 2 (Jari 2 di senar G)\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   | 3 |   |  <- Fret 3 (Jari 3 di senar B)\n"
                "  +---+---+---+---+---+---+\n"
                "  |   |   |   |   |   |   |  <- Fret 4\n"
                "  +---+---+---+---+---+---+\n"
                "    E   A   D   G   B   e"
            )
        }

        if kunci:
            kunci_clean = kunci.strip().lower()
            if kunci_clean in database_kunci:
                response_text = f"```\n{database_kunci[kunci_clean]}\n```"
                dispatcher.utter_message(text=response_text)
            else:
                dispatcher.utter_message(
                    text=f"Maaf, informasi untuk kunci '{kunci.upper()}' belum tersedia."
                )
        else:
            dispatcher.utter_message(
                text="Kunci gitar apa yang ingin kamu ketahui? (Contoh: Bm, C, G, Am, D)"
            )

        return []