# In market_view.py
import discord
import singletons
from commands.display.interactables.interactable import ItemListInteractable

def GetEmbedItemList(item_list, embed : discord.Embed, market : bool = False) -> discord.Embed:
    """Adds a neat item list to embed."""
    for item in item_list: # Iterates through to retrieve and use items on market.
        embed.add_field(name=f"• {item.name}" if market else f"• {item.name}\t({item.quantity})" , value=item.description, inline=True) # Field for Item name and description.
        embed.add_field(name=f"${item.cost}" if market else f"value ${item.cost}", value=" ", inline=True) # Field for cost.
        embed.add_field(name=" ", value=" ", inline=False) # Empty field as a seperator to make market more readable.

    return embed

class InventoryView(ItemListInteractable):
    def __init__(self, original_user, item_list, page, market = "Inventory", timeout=180):
        super().__init__(original_user=original_user, item_list=item_list, market=market, page=page, timeout=timeout)

class MarketView(ItemListInteractable):
    def __init__(self, original_user, item_list, market, page, timeout=180):
        super().__init__(original_user=original_user, item_list=item_list, market=market, page=page, timeout=timeout)


    @discord.ui.select(placeholder="Choose market: ", options=[
        discord.SelectOption(label="Market"),
        discord.SelectOption(label="Black Market")
    ])
    async def select_callback(self, interaction : discord.Interaction, select : discord.ui.Select):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        if select.values[0] == "Market":
            self.market = select.values[0]
            self.item_list = singletons.market_pages
            market = self.CreateListEmbed()
            view = MarketView(interaction.user, item_list=self.item_list, page=0, market=self.market) # Creates New ItemListView

            await interaction.response.edit_message(embed=market, view=view)

        elif select.values[0] == "Black Market":
            self.market = select.values[0]
            self.item_list = singletons.black_market_pages
            blackmarket = self.CreateListEmbed()
            view = MarketView(interaction.user, item_list=self.item_list, page=0, market=self.market) # Creates New ItemListView

            await interaction.response.edit_message(embed=blackmarket, view=view)

