import { useEffect, useState } from "react";

type Player = {
  name: string;
  team: string;
  score: number;
  reason: string;
};

export default function RecommendPage() {
  const [players, setPlayers] = useState<Player[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchRecommendations() {
      const res = await fetch("/api/recommend");
      const data = await res.json();
      setPlayers(data.players);
      setLoading(false);
    }

    fetchRecommendations();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-lg">Loading recommendations...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen max-w-4xl mx-auto px-6 py-10">
      <h1 className="text-3xl font-bold mb-6">
        🔥 Fantasy Pickup Recommendations
      </h1>

      <div className="space-y-4">
        {players.map((player, index) => (
          <div
            key={index}
            className="bg-white border rounded-lg p-4 shadow-sm"
          >
            <div className="flex justify-between items-center">
              <h2 className="text-xl font-semibold">
                {player.name} ({player.team})
              </h2>
              <span className="font-bold text-green-600">
                +{player.score}
              </span>
            </div>

            <p className="mt-2 text-gray-600">{player.reason}</p>
          </div>
        ))}
      </div>
    </div>
  );
}