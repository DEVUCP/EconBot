import discord

class interactable(discord.ui.View): # Parent class for all interactables.
    def __init__(self, original_user, timeout=180):
        super().__init__(timeout=timeout)
        self.original_user = original_user
        self.timeout = timeout

    def IsOriginalUser(self, user : discord.User) -> bool:
        """Returns True if user is the same as the original user."""
        return user.id == self.original_user.id

class ItemListInteractable(interactable): # For interactable lists of items.
    def __init__(self, original_user, item_list, market, page, timeout=180):
        super().__init__(original_user=original_user, timeout=timeout)
        self.item_list = item_list
        self.market = market
        self.current_page = page
        self.CreateListEmbed()

    @discord.ui.button(label="<<", style=discord.ButtonStyle.grey)
    async def FirstButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        self.current_page = 0
        await self.UpdateList(interaction)

    @discord.ui.button(label="<", style=discord.ButtonStyle.grey)
    async def PreviousButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        self.current_page = max(0, self.current_page - 1) # Picks 0 minimum if current_page is negative (invalid index).
        await self.UpdateList(interaction)

    @discord.ui.button(label=">", style=discord.ButtonStyle.grey)
    async def NextButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        self.current_page += 1 # Increment page.

         # If this index exists, then next page is valid.
        try :
            self.item_list[self.current_page]

        # if not then stay on last page.
        except IndexError: 
            self.current_page -= 1
        
        await self.UpdateList(interaction)

    @discord.ui.button(label=">>", style=discord.ButtonStyle.grey)
    async def Lastbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return
        
        self.current_page = len(self.item_list) - 1
        await self.UpdateList(interaction)


    async def UpdateList(self, interaction) -> None:
        """Update the list embed based on the current page"""
        new_embed = self.CreateListEmbed()
        await interaction.response.edit_message(embed=new_embed)
    
    def CreateListEmbed(self) -> discord.Embed:
        """Creates a list embed for the given page of the given item list"""

        embed = discord.Embed(
            title=self.market,
            description="You can buy stuff here." if self.market != "Inventory"
            else "All your items.",color=0xffff00
            ) # Create list Embed.

        embed = GetEmbedItemList(
            item_list=self.item_list[self.current_page],
            embed=embed,
            market=True if self.market!="Inventory" else False
            ) # Iterates through to retrieve and use items in list.
        
        embed.set_footer(text=f"Page {self.current_page}" if self.current_page >= 0 else f"Page {len(self.item_list) - 1}")

        return embed
        # Create and return the list embed for the given page
        # Use the existing logic from GetEmbedItemList, but paginate the items

def GetEmbedItemList(item_list, embed : discord.Embed, market : bool = False) -> discord.Embed:
    """Adds a neat item list to embed."""
    for item in item_list: # Iterates through to retrieve and use items on market.
        embed.add_field(name=f"• {item.name}" if market else f"• {item.name}\t({item.quantity})" , value=item.description, inline=True) # Field for Item name and description.
        embed.add_field(name=f"${item.cost}" if market else f"value ${item.cost}", value=" ", inline=True) # Field for cost.
        embed.add_field(name=" ", value=" ", inline=False) # Empty field as a seperator to make market more readable.

    return embed