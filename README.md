# MapleStory MCP Server

An MCP (Model Context Protocol) server that wraps the [Nexon MapleStory OpenAPI](https://open.api.nexon.com), allowing AI assistants to query MapleStory game data including character info, rankings, union, guild, and more.

## Features

- **Character** - Basic info, stats, equipment, skills, V/HEXA matrix, Dojang records
- **Union** - Union level, raider layout, artifact info
- **Guild** - Guild search and basic info
- **Ranking** - Overall, union, guild, Dojang, The Seed, achievement rankings
- **History** - Starforce, cube, potential re-roll history
- **Notice** - Official notices, updates, events, cash shop notices

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- MapleStory API key from [Nexon OpenAPI](https://open.api.nexon.com)

## Installation

```bash
# Clone the repository
git clone https://github.com/kcw2034/maplestory-mcp-server.git
cd maplestory-mcp-server

# Install dependencies
uv sync
```

## Configuration

Create a `.env` file in the project root:

```env
MAPLESTORY_API_KEY=your_api_key_here
```

You can get an API key by registering an app at [Nexon OpenAPI](https://open.api.nexon.com).

## Usage

### Running the server

```bash
uv run server.py
```

### Claude Desktop configuration

Add this to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "maplestory": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/path/to/maplestory-mcp-server",
      "env": {
        "MAPLESTORY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Available Tools

| Category | Tool | Description |
|----------|------|-------------|
| Character | `get_character_ocid` | Look up character OCID by name |
| Character | `get_character_basic` | Basic info (level, class, world, guild) |
| Character | `get_character_stat` | Combined stats (STR, DEX, combat power) |
| Character | `get_character_item_equipment` | Equipped items |
| Character | `get_character_skill` | Skill info by grade |
| Character | `get_character_hexamatrix` | HEXA matrix (6th job skills) |
| Union | `get_union` | Union level and grade |
| Union | `get_union_raider` | Union raider layout and effects |
| Guild | `get_guild_id` | Look up guild ID by name and world |
| Guild | `get_guild_basic` | Guild basic info |
| Ranking | `get_ranking_overall` | Overall ranking |
| Ranking | `get_ranking_dojang` | Mu Lung Dojang ranking |
| History | `get_history_starforce` | Starforce enhancement history |
| Notice | `get_notices` | Official notice list |

> See `server.py` for the full list of 30+ tools.

## License

[MIT](LICENSE)
