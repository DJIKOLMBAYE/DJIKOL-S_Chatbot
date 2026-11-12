import customtkinter as ctk


RESPONSES = {
    "bonjour!": "Bonjour! Comment puis-je vous aider aujourd'hui?",
    "comment ça va?": "Je suis un programme de Djikol's, donc je vais bien, merci! Et vous?",
    "quelle heure est-il?": (
        "Je suis désolé, je ne peux pas vous donner l'heure actuelle. "
        "Mais je crois qu'il est temps que vous vous mettiez à travailler "
        "sur votre projet de vie!"
    ),
    "avez-vous des conseils pour moi?": (
        "Bien sûr! Mon conseil est de toujours suivre votre passion et de ne "
        "jamais abandonner, même lorsque les choses deviennent difficiles. "
        "Avec de la détermination et du travail acharné, vous pouvez accomplir "
        "de grandes choses! C'est DJIKOLMBAYE qui vous le dit, soyez-en sûr."
    ),
    "merci!": "De rien! N'hésitez pas à me poser d'autres questions si vous en avez besoin.",
    "au revoir!": "Au revoir! Passez une excellente journée!",
}

FALLBACK_RESPONSE = (
    "Désolé, je n'ai pas compris votre message. Pouvez-vous reformuler?"
)


def chatbot_response(user_input: str) -> str:
    """Return a response for a case-insensitive, exact message match."""
    normalized_input = user_input.strip().casefold()
    return RESPONSES.get(normalized_input, FALLBACK_RESPONSE)


def create_app() -> ctk.CTk:
    app = ctk.CTk()
    app.geometry("600x500")
    app.minsize(480, 400)
    app.title("Chatbot de Djikol's")

    header = ctk.CTkLabel(
        app,
        text="Bienvenue dans le Chatbot de Djikol's",
        font=ctk.CTkFont(size=20, weight="bold"),
    )
    header.pack(pady=10)

    chat_history = ctk.CTkTextbox(
        app,
        height=320,
        state="disabled",
        font=("Arial", 16),
    )
    chat_history.tag_config("user", foreground="blue")
    chat_history.tag_config("bot", foreground="green")
    chat_history.pack(pady=10, padx=10, fill="both", expand=True)

    input_frame = ctk.CTkFrame(app)
    input_frame.pack(pady=10, padx=10, fill="x")

    entry_input = ctk.CTkEntry(
        input_frame,
        placeholder_text="Entrez votre message ici...",
    )
    entry_input.pack(side="left", padx=5, fill="x", expand=True)

    def send_message(_event: object | None = None) -> str:
        user_message = entry_input.get()
        if not user_message.strip():
            return "break"

        chat_history.configure(state="normal")
        chat_history.insert("end", f"Vous: {user_message}\n", "user")
        chat_history.insert(
            "end",
            f"Chatbot: {chatbot_response(user_message)}\n",
            "bot",
        )
        chat_history.configure(state="disabled")
        chat_history.see("end")
        entry_input.delete(0, "end")
        return "break"

    send_button = ctk.CTkButton(
        input_frame,
        text="Envoyer",
        command=send_message,
    )
    send_button.pack(side="left", padx=5)

    entry_input.bind("<Return>", send_message)
    return app


def main() -> None:
    create_app().mainloop()


if __name__ == "__main__":
    main()
