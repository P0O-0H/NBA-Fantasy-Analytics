export default function PickupCard({ player }: any) {
    return (
      <div className="bg-white p-5 rounded-xl shadow hover:shadow-lg transition">
        <div className="flex justify-between">
          <div>
            <h2 className="text-lg font-semibold">{player.name}</h2>
            <p className="text-sm text-gray-500">{player.team}</p>
          </div>
          <span className="text-purple-600 font-bold text-xl">
            +{player.score}
          </span>
        </div>
        <p className="mt-3 text-gray-700">{player.reason}</p>
      </div>
    );
  }
