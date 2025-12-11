import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import PickupCard from "../components/PickupCard";

export default function Home() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    async function load() {
      const res = await fetch("/api/recommend");
      const data = await res.json();
      setPlayers(data.players);
    }
    load();
  }, []);

  return (
    <Layout>
      <h1 className="text-3xl font-bold mb-6">Top Fantasy Pickups Today</h1>

      <div className="grid gap-4">
        {players.map((p: any) => (
          <PickupCard key={p.name} player={p} />
        ))}
      </div>
    </Layout>
  );
}
