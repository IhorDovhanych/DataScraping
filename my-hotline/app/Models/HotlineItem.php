<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class HotlineItem extends Model
{
    use HasFactory;
    protected $table = 'items';
    protected $fillable = [
        'name',
        'price',
        'url',
        'image_urls',
        'img'
    ];
}
