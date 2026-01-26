import { useState } from "react";

type Player = {
  player_id: number;
  name: string;
  team?: string | null;        // e.g. "LAL", "BOS"
  score: number;
  recent_fp: number;
  minutes_trend: number;
  upside: number;
};

export default function PickupCard({ player }: { player: Player }) {
  const [open, setOpen] = useState(false);

  // NBA team logo via ESPN CDN (very reliable)
  const teamLogo = player.team
    ? `https://a.espncdn.com/i/teamlogos/nba/500/${player.team}.png`
    : null;

  return (
    <div
      onClick={() => setOpen(!open)}
      className="bg-white p-5 rounded-xl shadow hover:shadow-lg transition cursor-pointer"
    >
      {/* Header */}
      <div className="flex justify-between items-center">
        <div className="flex items-center gap-4">
          {/* Team logo */}
          {teamLogo ? (
            <img
              src={teamLogo}
              alt={player.team ?? "Team"}
              className="w-12 h-12 object-contain"
              onError={(e) => {
                e.currentTarget.style.display = "none";
              }}
            />
          ) : (
            <div className="w-12 h-12 bg-gray-200 rounded flex items-center justify-center text-xs text-gray-500">
              N/A
            </div>
          )}

          {/* Player info */}
          <div>
            <h2 className="text-lg font-semibold">{player.name}</h2>
            <p className="text-sm text-gray-500">
              {player.team ?? "Unknown team"}
            </p>
          </div>
        </div>

        {/* Recommendation score */}
        <span className="text-purple-600 font-bold text-xl">
          {player.score.toFixed(1)}
        </span>
      </div>

      {/* Metrics row */}
      <div className="grid grid-cols-3 gap-4 mt-4 text-sm">
        <div>
          <p className="text-gray-400">Recent FP</p>
          <p className="font-semibold">{player.recent_fp !== undefined ? player.recent_fp.toFixed(1) : "—"}</p>
        </div>

        <div>
          <p className="text-gray-400">Minutes</p>
          <p className="font-semibold">{player.minutes_trend !== undefined ? player.minutes_trend.toFixed(1): "—"}</p>
        </div>

        <div>
          <p className="text-gray-400">Upside</p>
          <p className="font-semibold text-green-600">
            +{player.upside?.toFixed(1) ?? "—"}
          </p>
        </div>
      </div>

      {/* Expandable explanation */}
      {open && (
        <div className="mt-4 text-sm text-gray-600 border-t pt-3 space-y-1">
          <p>📈 Recent fantasy form above baseline</p>
          <p>⏱ Minutes trend supports role stability</p>
          <p>🎯 Upside captures volatility + opportunity</p>
        </div>
      )}
    </div>
  );
}