"""
Couche de sécurité basée uniquement sur le framework NeMo Guardrails.

Aucune règle n'est écrite à la main dans ce fichier : toute la politique de sécurité
est déclarée dans le dossier config/ :
  - config/config.yml  : modèle, rails d'entrée et rails de sortie activés
  - config/prompts.yml : consignes données au modèle juge (self check input / output)
"""
from nemoguardrails import LLMRails, RailsConfig

# Message de refus par défaut de NeMo Guardrails quand un rail bloque la requête
REFUSAL = "I'm sorry, I can't respond to that."


def build_rails(config_path: str = "./config") -> LLMRails:
    """Charge la configuration NeMo Guardrails et crée l'objet qui applique les rails."""
    config = RailsConfig.from_path(config_path)
    return LLMRails(config)


def secure_generate(rails: LLMRails, message: str) -> str:
    """Envoie le message à travers les rails : entrée -> modèle -> sortie."""
    response = rails.generate(messages=[{"role": "user", "content": message}])
    return response["content"]