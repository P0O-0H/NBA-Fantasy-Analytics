import { useState } from "react";
import Image from "next/image";

type Player = {
  player_id: number;
  name: string;
  team?: string | null;        // e.g. "LAL", "BOS"
  score: number;
  recent_fp: number;
  minutes_trend: number;
  upside: number;
  form_score: number;
  minute_score: number;
  usage_score: number;
};

export default function PickupCard({ player }: { player: Player }) {
  const [open, setOpen] = useState(false);

  // NBA team logo via ESPN CDN (very reliable)
  const teamLogo = player.team
    ? `https://a.espncdn.com/i/teamlogos/nba/500/${player.team}.png`
    : null;

    const headshot = `https://cdn.nba.com/headshots/nba/latest/260x190/${player.player_id}.png`;


    return (
      <div
        onClick={() => setOpen(!open)}
        className="bg-white p-5 rounded-xl shadow hover:shadow-lg transition cursor-pointer"
      >
        {/* ================= Header ================= */}
        <div className="flex justify-between items-center">
          <div className="flex items-center gap-4">
            
            {/* Player Headshot */}
            <Image
            src={`https://cdn.nba.com/headshots/nba/latest/260x190/${player.player_id}.png`}
            alt={player.name}
            width={56}
            height={56}
            unoptimized
            className="rounded-full object-cover border bg-gray-200"
          />
  
            {/* Player Info */}
            <div>
              <h2 className="text-lg font-semibold">{player.name}</h2>
              <div className="flex items-center gap-2 text-sm text-gray-500">
                {teamLogo && (
                  <img
                    src={teamLogo}
                    alt={player.team ?? "Team"}
                    className="w-5 h-5 object-contain"
                    onError={(e) => {
                      e.currentTarget.src = "/player-placeholder.png";
                    }}
                  />
                )}
                <span>{player.team ?? "Unknown team"}</span>
              </div>
            </div>
          </div>
  
          {/* Recommendation Score */}
          <span className="text-purple-600 font-bold text-xl">
            {Number.isFinite(player.score) ? player.score.toFixed(1) : "—"}
          </span>
        </div>
  
        {/* ================= Metrics ================= */}
        <div className="grid grid-cols-3 gap-4 mt-4 text-sm">
          <div>
            <p className="text-gray-400">Recent FP</p>
            <p className="font-semibold">
              {Number.isFinite(player.recent_fp)
                ? player.recent_fp!.toFixed(1)
                : "—"}
            </p>
          </div>
  
          <div>
            <p className="text-gray-400">Minutes</p>
            <p className="font-semibold">
              {Number.isFinite(player.minutes_trend)
                ? player.minutes_trend!.toFixed(1)
                : "—"}
            </p>
          </div>
  
          <div>
            <p className="text-gray-400">Upside</p>
            <p
              className={`font-semibold ${
                Number.isFinite(player.upside) && player.upside! > 0
                  ? "text-green-600"
                  : "text-gray-500"
              }`}
            >
              {Number.isFinite(player.upside)
                ? `+${player.upside!.toFixed(1)}`
                : "—"}
            </p>
          </div>
        </div>
  
        {/* ================= Expandable Explanation ================= */}
        {open && (
          <div className="mt-4 text-sm text-gray-600 border-t pt-3 space-y-1">
            <p>📈 Form signal: {player.form_score.toFixed(1)}</p>
            <p>⏱ Minutes signal: {player.minute_score.toFixed(1)}</p>
            <p>🔥 Usage signal: {player.usage_score.toFixed(1)}</p>
          </div>
        )}
      </div>
    );
  }