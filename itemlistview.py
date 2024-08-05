# In shop_view.py
import discord
import utils

class ItemListView(discord.ui.View):
    def __init__(self, original_user, item_list, shop = False, timeout=180):
        super().__init__(timeout=timeout)
        self.original_user = original_user
        self.item_list = item_list
        self.shop = shop
        self.current_page = 0

    def IsOriginalUser(self, user : discord.User) -> bool:
        """Returns True if user is the same as the original user."""
        return user.id == self.original_user.id

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
        new_embed = CreateListEmbed(page=self.current_page, item_list=self.item_list, shop=self.shop)
        await interaction.response.edit_message(embed=new_embed)


def CreateListEmbed(page : int, item_list, shop : bool = False) -> discord.Embed:
    embed = discord.Embed(title="Market" if shop else "Inventory",description="You can buy stuff here." if shop else "All your items.",color=0xffff00) # Create list Embed.
    embed = utils.GetEmbedItemList(item_list=item_list[page], embed=embed, shop=shop) # Iterates through to retrieve and use items in list.
    embed.set_footer(text=f"Page {page}" if page >= 0 else f"Page {len(item_list) - 1}")
    return embed
    # Create and return the list embed for the given page
    # Use the existing logic from GetEmbedItemList, but paginate the items