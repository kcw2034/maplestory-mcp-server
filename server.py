import os
from typing import Annotated

import httpx
from fastmcp import FastMCP

mcp = FastMCP("MapleStory MCP Server")

BASE_URL = "https://open.api.nexon.com"
API_KEY = os.environ.get("MAPLESTORY_API_KEY", "")


async def _request(path: str, params: dict | None = None) -> dict:
    """Send a GET request to the MapleStory OpenAPI."""
    if not API_KEY:
        return {"error": "MAPLESTORY_API_KEY 환경변수가 설정되지 않았습니다."}
    headers = {"x-nxopen-api-key": API_KEY}
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{BASE_URL}{path}",
            headers=headers,
            params={k: v for k, v in (params or {}).items() if v is not None},
            timeout=30.0,
        )
        if resp.status_code != 200:
            return {"error": f"API 요청 실패 (HTTP {resp.status_code})", "detail": resp.text}
        return resp.json()


# ──────────────────────────────────────────────
# Character ID
# ──────────────────────────────────────────────

@mcp.tool
async def get_character_ocid(
    character_name: Annotated[str, "캐릭터 이름"],
) -> dict:
    """캐릭터 이름으로 OCID(캐릭터 식별자)를 조회합니다. 다른 캐릭터 정보 조회에 필요한 값입니다."""
    return await _request("/maplestory/v1/id", {"character_name": character_name})


# ──────────────────────────────────────────────
# Character Information
# ──────────────────────────────────────────────

@mcp.tool
async def get_character_basic(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD). 미입력 시 최근 데이터 조회"] = None,
) -> dict:
    """캐릭터 기본 정보(레벨, 직업, 월드, 길드, 캐릭터 이미지 등)를 조회합니다."""
    return await _request("/maplestory/v1/character/basic", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_stat(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 종합 스탯(STR, DEX, 전투력 등)을 조회합니다."""
    return await _request("/maplestory/v1/character/stat", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_popularity(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 인기도를 조회합니다."""
    return await _request("/maplestory/v1/character/popularity", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_hyper_stat(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 하이퍼스탯 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/hyper-stat", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_propensity(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 성향 정보(카리스마, 매력 등)를 조회합니다."""
    return await _request("/maplestory/v1/character/propensity", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_ability(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 어빌리티(내부 능력) 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/ability", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_item_equipment(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 장착 장비 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/item-equipment", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_cashitem_equipment(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 캐시 장비 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/cashitem-equipment", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_symbol_equipment(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 심볼(아케인/어센틱) 장비 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/symbol-equipment", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_set_effect(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 적용 세트 효과 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/set-effect", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_beauty_equipment(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 헤어/성형/피부 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/beauty-equipment", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_android_equipment(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 안드로이드 장비 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/android-equipment", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_pet_equipment(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 펫 장비 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/pet-equipment", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_skill(
    ocid: Annotated[str, "캐릭터 OCID"],
    character_skill_grade: Annotated[str, "스킬 차수 (0~6, hyperpassive, hyperactive)"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 스킬 정보를 조회합니다. character_skill_grade: 0=1차, 1=2차, ..., 5=5차, 6=6차, hyperpassive, hyperactive"""
    return await _request("/maplestory/v1/character/skill", {
        "ocid": ocid, "character_skill_grade": character_skill_grade, "date": date,
    })


@mcp.tool
async def get_character_link_skill(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 링크 스킬 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/link-skill", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_vmatrix(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 V매트릭스(5차 스킬 코어) 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/vmatrix", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_hexamatrix(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 HEXA매트릭스(6차 스킬) 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/hexamatrix", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_hexamatrix_stat(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 HEXA 스탯 정보를 조회합니다."""
    return await _request("/maplestory/v1/character/hexamatrix-stat", {"ocid": ocid, "date": date})


@mcp.tool
async def get_character_dojang(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """캐릭터 무릉도장 최고 기록을 조회합니다."""
    return await _request("/maplestory/v1/character/dojang", {"ocid": ocid, "date": date})


# ──────────────────────────────────────────────
# Union
# ──────────────────────────────────────────────

@mcp.tool
async def get_union(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """유니온 레벨 및 등급 정보를 조회합니다."""
    return await _request("/maplestory/v1/user/union", {"ocid": ocid, "date": date})


@mcp.tool
async def get_union_raider(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """유니온 공격대 배치 및 효과 정보를 조회합니다."""
    return await _request("/maplestory/v1/user/union-raider", {"ocid": ocid, "date": date})


@mcp.tool
async def get_union_artifact(
    ocid: Annotated[str, "캐릭터 OCID"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """유니온 아티팩트 정보를 조회합니다."""
    return await _request("/maplestory/v1/user/union-artifact", {"ocid": ocid, "date": date})


# ──────────────────────────────────────────────
# Guild
# ──────────────────────────────────────────────

@mcp.tool
async def get_guild_id(
    guild_name: Annotated[str, "길드 이름"],
    world_name: Annotated[str, "월드 이름 (스카니아, 베라, 루나, 리부트 등)"],
) -> dict:
    """길드 이름과 월드명으로 길드 식별자(oguild_id)를 조회합니다."""
    return await _request("/maplestory/v1/guild/id", {
        "guild_name": guild_name, "world_name": world_name,
    })


@mcp.tool
async def get_guild_basic(
    oguild_id: Annotated[str, "길드 식별자 (oguild_id)"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
) -> dict:
    """길드 기본 정보(멤버, 스킬 등)를 조회합니다."""
    return await _request("/maplestory/v1/guild/basic", {"oguild_id": oguild_id, "date": date})


# ──────────────────────────────────────────────
# Ranking
# ──────────────────────────────────────────────

@mcp.tool
async def get_ranking_overall(
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    world_name: Annotated[str | None, "월드 이름"] = None,
    world_type: Annotated[str | None, "월드 타입 (0: 일반, 1: 리부트)"] = None,
    class_: Annotated[str | None, "직업 (전사, 마법사, 궁수 등)"] = None,
    ocid: Annotated[str | None, "특정 캐릭터 OCID"] = None,
    page: Annotated[int | None, "페이지 번호"] = None,
) -> dict:
    """종합 랭킹을 조회합니다."""
    return await _request("/maplestory/v1/ranking/overall", {
        "date": date, "world_name": world_name, "world_type": world_type,
        "class": class_, "ocid": ocid, "page": page,
    })


@mcp.tool
async def get_ranking_union(
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    world_name: Annotated[str | None, "월드 이름"] = None,
    ocid: Annotated[str | None, "특정 캐릭터 OCID"] = None,
    page: Annotated[int | None, "페이지 번호"] = None,
) -> dict:
    """유니온 랭킹을 조회합니다."""
    return await _request("/maplestory/v1/ranking/union", {
        "date": date, "world_name": world_name, "ocid": ocid, "page": page,
    })


@mcp.tool
async def get_ranking_guild(
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    world_name: Annotated[str | None, "월드 이름"] = None,
    ranking_type: Annotated[str | None, "랭킹 타입 (0: 주간, 1: 플래그, 2: 지하수로)"] = None,
    guild_name: Annotated[str | None, "길드 이름"] = None,
    page: Annotated[int | None, "페이지 번호"] = None,
) -> dict:
    """길드 랭킹을 조회합니다."""
    return await _request("/maplestory/v1/ranking/guild", {
        "date": date, "world_name": world_name, "ranking_type": ranking_type,
        "guild_name": guild_name, "page": page,
    })


@mcp.tool
async def get_ranking_dojang(
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    world_name: Annotated[str | None, "월드 이름"] = None,
    class_: Annotated[str | None, "직업"] = None,
    ocid: Annotated[str | None, "특정 캐릭터 OCID"] = None,
    page: Annotated[int | None, "페이지 번호"] = None,
) -> dict:
    """무릉도장 랭킹을 조회합니다."""
    return await _request("/maplestory/v1/ranking/dojang", {
        "date": date, "world_name": world_name, "class": class_,
        "ocid": ocid, "page": page,
    })


@mcp.tool
async def get_ranking_theseed(
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    world_name: Annotated[str | None, "월드 이름"] = None,
    ocid: Annotated[str | None, "특정 캐릭터 OCID"] = None,
    page: Annotated[int | None, "페이지 번호"] = None,
) -> dict:
    """더 시드 랭킹을 조회합니다."""
    return await _request("/maplestory/v1/ranking/theseed", {
        "date": date, "world_name": world_name, "ocid": ocid, "page": page,
    })


@mcp.tool
async def get_ranking_achievement(
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    ocid: Annotated[str | None, "특정 캐릭터 OCID"] = None,
    page: Annotated[int | None, "페이지 번호"] = None,
) -> dict:
    """업적 랭킹을 조회합니다."""
    return await _request("/maplestory/v1/ranking/achievement", {
        "date": date, "ocid": ocid, "page": page,
    })


# ──────────────────────────────────────────────
# History
# ──────────────────────────────────────────────

@mcp.tool
async def get_history_starforce(
    count: Annotated[int, "한 번에 조회할 건수"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    cursor: Annotated[str | None, "이전 응답의 next_cursor 값"] = None,
) -> dict:
    """스타포스 강화 이력을 조회합니다."""
    return await _request("/maplestory/v1/history/starforce", {
        "count": count, "date": date, "cursor": cursor,
    })


@mcp.tool
async def get_history_cube(
    count: Annotated[int, "한 번에 조회할 건수"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    cursor: Annotated[str | None, "이전 응답의 next_cursor 값"] = None,
) -> dict:
    """큐브 사용 이력을 조회합니다."""
    return await _request("/maplestory/v1/history/cube", {
        "count": count, "date": date, "cursor": cursor,
    })


@mcp.tool
async def get_history_potential(
    count: Annotated[int, "한 번에 조회할 건수"],
    date: Annotated[str | None, "조회 기준일 (YYYY-MM-DD)"] = None,
    cursor: Annotated[str | None, "이전 응답의 next_cursor 값"] = None,
) -> dict:
    """잠재능력 재설정 이력을 조회합니다."""
    return await _request("/maplestory/v1/history/potential", {
        "count": count, "date": date, "cursor": cursor,
    })


# ──────────────────────────────────────────────
# Notice
# ──────────────────────────────────────────────

@mcp.tool
async def get_notices() -> dict:
    """메이플스토리 공지사항 목록을 조회합니다."""
    return await _request("/maplestory/v1/notice")


@mcp.tool
async def get_notice_detail(
    notice_id: Annotated[int, "공지사항 ID"],
) -> dict:
    """특정 공지사항 상세 내용을 조회합니다."""
    return await _request("/maplestory/v1/notice/detail", {"notice_id": notice_id})


@mcp.tool
async def get_update_notices() -> dict:
    """업데이트 공지 목록을 조회합니다."""
    return await _request("/maplestory/v1/notice-update")


@mcp.tool
async def get_event_notices() -> dict:
    """이벤트 공지 목록을 조회합니다."""
    return await _request("/maplestory/v1/notice-event")


@mcp.tool
async def get_cashshop_notices() -> dict:
    """캐시샵 공지 목록을 조회합니다."""
    return await _request("/maplestory/v1/notice-cashshop")


if __name__ == "__main__":
    mcp.run()
